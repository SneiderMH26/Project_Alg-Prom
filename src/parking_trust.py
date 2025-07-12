# PARKING TRUST - SISTEMA DE PARQUEADERO UNIVERSITARIO

!pip install pytz
import csv
import os
import platform
import time
from datetime import datetime
import pytz

zona_colombia = pytz.timezone("America/Bogota")

# ======================== VARIABLES GLOBALES ============================
usuarios_registrados = []
vehiculos_en_parqueo = []
vehiculos_retirados = []

log_file = "log_eventos.txt"
usuarios_csv = "usuarios.csv"
ESPACIOS_DISPONIBLES = 64

empleados = {
    "empleado1": "turno1",
    "empleado2": "turno2",
    "empleado3": "turno3"
}

admin_credenciales = {
    "admin": "1234"
}

# ======================== FUNCIONES UTILITARIAS ============================

import getpass

def log_evento(accion, inicio, usuario='Sistema'):
    fin = time.time()
    duracion = round((fin - inicio), 4)
    fecha = datetime.now(zona_colombia).strftime("%Y-%m-%d")
    hora = datetime.now(zona_colombia).strftime("%H:%M:%S.%f")[:-3]
    sistema = platform.system()
    version = platform.version()
    plataforma = platform.platform()
    usuario_so = getpass.getuser()

    encabezado = f"Usuario: {usuario_so} | Sistema: {sistema} | Plataforma: {plataforma} | Versión: {version}"
    if not os.path.exists(log_file):
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(encabezado + "\n")
            f.write("Fecha\tHora\t\t\tAcción\t\t\tDuración (s)\n")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{fecha}\t{hora}\t{accion}\t{duracion}\n")


def exportar_usuarios_csv():
    with open(usuarios_csv, "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["nombre", "apellido", "documento", "placa", "hora_registro"])
        writer.writeheader()
        for user in usuarios_registrados:
            writer.writerow(user)


def exportar_vehiculos_retirados_csv():
    with open("vehiculos_retirados.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "documento", "placa", "hora_ingreso", "hora_salida", "minutos_total", "total_pagar"
        ])
        writer.writeheader()
        for v in vehiculos_retirados:
            writer.writerow(v)


def exportar_informe_retirados_csv():
    with open("informe_vehiculos_retirados.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "nombre", "apellido", "documento", "placa", "hora_ingreso", "hora_salida", "minutos_total", "total_pagar"
        ])
        writer.writeheader()
        for v in vehiculos_retirados:
            # Buscar usuario por documento
            usuario = next((u for u in usuarios_registrados if u["documento"] == v["documento"]), {})
            writer.writerow({
                "nombre": usuario.get("nombre", "Desconocido"),
                "apellido": usuario.get("apellido", "Desconocido"),
                "documento": v["documento"],
                "placa": v["placa"],
                "hora_ingreso": v["hora_ingreso"],
                "hora_salida": v["hora_salida"],
                "minutos_total": v["minutos_total"],
                "total_pagar": v["total_pagar"]
            })

# ======================== MÓDULO 1: REGISTRAR USUARIO ============================

def validar_nombre(nombre):
    if len(nombre) < 3:
        return "El nombre debe tener mínimo 3 letras."
    if not nombre.isalpha():
        return "El nombre no debe contener números ni símbolos."
    return None

def validar_apellido(apellido):
    if len(apellido) < 3:
        return "El apellido debe tener mínimo 3 letras."
    if not apellido.isalpha():
        return "El apellido no debe contener números ni símbolos."
    return None

def validar_documento(doc):
    if not doc.isdigit():
        return "El documento solo puede contener números."
    if not (3 <= len(doc) <= 15):
        return "El documento debe tener entre 3 y 15 dígitos."
    return None

def validar_placa(placa):
    if len(placa) != 6:
        return "La placa debe tener exactamente 6 caracteres."
    if not (placa[:3].isalpha() and placa[3:].isdigit()):
        return "La placa debe tener el formato AAA123 (3 letras + 3 números)."
    return None

def registrar_usuario():
    while True:
        print("\n REGISTRO DE USUARIO")
        inicio = time.time()
        nombre = input("Nombre: ").strip().capitalize()
        apellido = input("Apellido: ").strip().capitalize()
        documento = input("Documento (solo números): ").strip()
        placa = input("Placa (AAA123): ").strip().upper()

        errores = []
        for valor, validador in [(nombre, validar_nombre), (apellido, validar_apellido),
                                 (documento, validar_documento), (placa, validar_placa)]:
            error = validador(valor)
            if error:
                errores.append(error)

        if errores:
            print("\n ERRORES DETECTADOS:")
            for e in errores:
                print(f" - {e}")
            continue

        usuario = {
            "nombre": nombre,
            "apellido": apellido,
            "documento": documento,
            "placa": placa,
            "hora_registro": datetime.now(zona_colombia).strftime("%Y-%m-%d %H:%M:%S")
        }
        usuarios_registrados.append(usuario)
        exportar_usuarios_csv()
        log_evento("Registrar Usuario", inicio, documento)
        print(f"\n Usuario {nombre} {apellido} registrado correctamente.\n")
        break
# ======================== MÓDULO 2: INGRESAR VEHÍCULO ============================

def usuario_existe(documento, placa):
    return any(u["documento"] == documento and u["placa"] == placa for u in usuarios_registrados)

def ingresar_vehiculo():
    global vehiculos_en_parqueo

    print("\n INGRESO DE VEHÍCULO")
    inicio = time.time()
    documento = input("Ingrese el documento del usuario: ").strip()
    placa = input("Ingrese la placa del vehículo (AAA123): ").strip().upper()

    if not usuario_existe(documento, placa):
        print("\n Usuario no registrado o placa no coincide.")
        print("Debe registrar el usuario antes de ingresar el vehículo.")
        return

    if len(vehiculos_en_parqueo) >= ESPACIOS_DISPONIBLES:
        print("\n Parqueadero lleno. No hay espacios disponibles.")
        return

    if any(v["placa"] == placa for v in vehiculos_en_parqueo):
        print("\n Este vehículo ya está registrado como ingresado.")
        return

    hora_ingreso = datetime.now(zona_colombia)
    vehiculo = {
        "documento": documento,
        "placa": placa,
        "hora_ingreso": hora_ingreso,
        "hora_ingreso_str": hora_ingreso.strftime("%Y-%m-%d %H:%M:%S")
    }
    vehiculos_en_parqueo.append(vehiculo)
    log_evento("Ingresar Vehículo", inicio, documento)

    print("\n Vehículo ingresado correctamente.")
    print(f" Recibo (Sello): {hora_ingreso.strftime('%H:%M')} - Placa: {placa}")

# ======================== MÓDULO 3: RETIRAR VEHÍCULO ============================

def calcular_pago(minutos_totales):
    horas = minutos_totales // 60
    minutos_restantes = minutos_totales % 60
    cuartos = (minutos_restantes + 14) // 15  # redondeo hacia arriba
    total = horas * 7000 + cuartos * 1500
    return max(total, 7000)  # mínimo 7000 pesos

def retirar_vehiculo():
    global vehiculos_en_parqueo, vehiculos_retirados

    print("\n RETIRO DE VEHÍCULO")
    inicio = time.time()
    documento = input("Ingrese el documento del usuario: ").strip()
    placa = input("Ingrese la placa del vehículo (AAA123): ").strip().upper()

    vehiculo = None
    for v in vehiculos_en_parqueo:
        if v["documento"] == documento and v["placa"] == placa:
            vehiculo = v
            break

    if not vehiculo:
        print("\n No se encontró un vehículo ingresado con esos datos.")
        return

    hora_ingreso = vehiculo["hora_ingreso"]
    hora_salida = datetime.now(zona_colombia)
    minutos_total = int((hora_salida - hora_ingreso).total_seconds() // 60)
    total_a_pagar = calcular_pago(minutos_total)

    vehiculos_en_parqueo.remove(vehiculo)
    vehiculo_retirado = {
        "documento": documento,
        "placa": placa,
        "hora_ingreso": hora_ingreso.strftime("%Y-%m-%d %H:%M:%S"),
        "hora_salida": hora_salida.strftime("%Y-%m-%d %H:%M:%S"),
        "minutos_total": minutos_total,
        "total_pagar": total_a_pagar
    }
    vehiculos_retirados.append(vehiculo_retirado)
    exportar_vehiculos_retirados_csv()
    exportar_informe_retirados_csv()


    log_evento("Retirar Vehículo", inicio, documento)

    print("\n Vehículo retirado exitosamente.")
    print(" Factura")
    print(f" Ingreso: {vehiculo_retirado['hora_ingreso']}")
    print(f" Salida : {vehiculo_retirado['hora_salida']}")
    print(f" Tiempo Total: {minutos_total} minutos")
    print(f" Total a pagar: ${total_a_pagar:,.0f} COP")

# ======================== MÓDULO 4: ADMINISTRADOR ============================

def admin_menu():
    while True:
        print("""
SUBMENÚ DE ADMINISTRACIÓN
1. Total de vehículos registrados
2. Total de vehículos retirados
3. Total de vehículos sin retirar
4. Total pagos recibidos
5. Tiempo promedio de estancia
6. Lista de usuarios
7. Vehículo con mayor y menor tiempo
8. Volver al menú principal
        """)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print(f" Total de vehículos registrados: {len(usuarios_registrados)}")
        elif opcion == "2":
            print(f" Vehículos retirados: {len(vehiculos_retirados)}")
        elif opcion == "3":
            print(f" Vehículos sin retirar: {len(vehiculos_en_parqueo)}")
        elif opcion == "4":
            total_pagado = sum(v["total_pagar"] for v in vehiculos_retirados)
            print(f" Total pagos recibidos: ${total_pagado:,.0f} COP")
        elif opcion == "5":
            if vehiculos_retirados:
                promedio = sum(v["minutos_total"] for v in vehiculos_retirados) / len(vehiculos_retirados)
                print(f" Tiempo promedio de estancia: {promedio:.2f} minutos")
            else:
                print(" No hay vehículos retirados aún.")
        elif opcion == "6":
            print("\n Lista de Usuarios Registrados:")
            for i, u in enumerate(usuarios_registrados, 1):
                print(f"{i}. {u['nombre']} {u['apellido']} - Doc: {u['documento']} - Placa: {u['placa']}")
        elif opcion == "7":
            if not vehiculos_retirados:
                print(" Aún no hay vehículos retirados.")
                continue
            ordenados = sorted(vehiculos_retirados, key=lambda v: v["minutos_total"])
            menor = ordenados[0]
            mayor = ordenados[-1]
            print(f" Tiempo mínimo: {menor['placa']} - {menor['minutos_total']} min")
            print(f" Tiempo máximo: {mayor['placa']} - {mayor['minutos_total']} min")
        elif opcion == "8":
            print(" Regresando al menú principal...\n")
            break
        else:
            print(" Opción inválida.")

def admin_login():
    print("\n ACCESO ADMINISTRADOR")
    user = input("Usuario: ").strip()
    pwd = input("Contraseña: ").strip()

    if user in admin_credenciales and admin_credenciales[user] == pwd:
        print(" Acceso concedido.")
        admin_menu()
    else:
        print(" Usuario o contraseña incorrectos.")

# ======================== MÓDULO 5: LOGIN Y SALIR ============================

def inicio_sesion():
    while True:
        print("\n SISTEMA PARKING TRUST - INICIO DE SESIÓN")
        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()

        if usuario in empleados and empleados[usuario] == contraseña:
            log_evento("Inicio de sesión", time.time(), usuario)
            print(f"\n Bienvenido, {usuario}.\n")
            menu_principal()
            break
        else:
            print(" Usuario o contraseña inválidos. Intente de nuevo.\n")

def menu_principal():
    while True:
        print("""
╔════════════════════════════╗
║     MENÚ PRINCIPAL         ║
╠════════════════════════════╣
║ 1. Registrar Usuario       ║
║ 2. Ingresar Vehículo       ║
║ 3. Retirar Vehículo        ║
║ 4. Administrador           ║
║ 5. Salir                   ║
╚════════════════════════════╝
        """)
        op = input("Seleccione una opción: ").strip()

        if op == "1":
            registrar_usuario()
        elif op == "2":
            ingresar_vehiculo()
        elif op == "3":
            retirar_vehiculo()
        elif op == "4":
            admin_login()
        elif op == "5":
            print(" Cerrando sesión...\n")
            log_evento("Cierre de sesión", time.time())
            inicio_sesion()
            break
        else:
            print(" Opción inválida.")

# ======================== INICIO DEL PROGRAMA ============================
inicio_sesion()
