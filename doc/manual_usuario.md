# Manual de Usuario – Sistema Parking Trust

## Descripción general

**Parking Trust** es un sistema de consola en Python que permite gestionar el funcionamiento básico de un parqueadero universitario. El sistema simula las operaciones más comunes: registro de usuarios, ingreso y salida de vehículos, cálculo del tiempo de parqueo y cobro automático, así como reportes administrativos para la gestión del parqueadero.

Está diseñado para ser ejecutado desde una terminal o consola de comandos y cuenta con menús interactivos, validaciones y exportación de información en archivos `.csv`.

## Requisitos del sistema

- **Python 3.8 o superior**
- Librerías estándar de Python: `csv`, `datetime`, `time`, `getpass`, `os`, `platform`
- Librería adicional: `pytz` (para ajustar la hora a la zona de Bogotá)
  - Se instala con: `pip install pytz`

---

## Inicio de sesión

Al iniciar el sistema, se pedirá un **usuario y contraseña de empleado**. Se puede usar cualquiera de los siguientes:

| Usuario     | Contraseña |
|-------------|------------|
| empleado1   | turno1     |
| empleado2   | turno2     |
| empleado3   | turno3     |

También hay un **usuario administrador** para acceder a reportes:

- Usuario: `admin`
- Contraseña: `1234`

## Navegación por el sistema

Al ingresar, el usuario verá el siguiente **menú principal**:

╔════════════════════════════╗
║     MENÚ PRINCIPAL         ║
╠════════════════════════════╣
║ 1. Registrar Usuario       ║
║ 2. Ingresar Vehículo       ║
║ 3. Retirar Vehículo        ║
║ 4. Administrador           ║
║ 5. Salir                   ║
╚════════════════════════════╝

## Registrar Usuario

Permite ingresar los datos del cliente que usará el parqueadero:

- Nombre (mínimo 3 letras, sin números)
- Apellido (mínimo 3 letras, sin números)
- Documento (solo números, entre 3 y 15 dígitos)
- Placa del vehículo (formato AAA123, 3 letras y 3 números)

Se valida cada dato antes de aceptar el registro. Si es correcto, se guarda en memoria y se exporta a `usuarios.csv`.

## Ingresar Vehículo

Solo usuarios previamente registrados pueden ingresar vehículos.  
El sistema validará que haya espacio en el parqueadero (máximo 64 espacios).  
Al ingresar correctamente, se guarda la hora de entrada y se genera un recibo visual con hora y placa.

## Retirar Vehículo

Permite calcular el valor a pagar con base en el tiempo transcurrido:

- 💲 **7000 COP por hora completa**
- 💲 **1500 COP por cada fracción de 15 minutos**
- 💲 **Pago mínimo: 7000 COP**

También se muestra un recibo en pantalla con:
- Hora de ingreso
- Hora de salida
- Tiempo total
- Total a pagar

Los datos se exportan a:
- `vehiculos_retirados.csv`
- `informe_vehiculos_retirados.csv`

---

## Módulo Administrador

Solo accesible con usuario `admin`. Permite:

- Ver totales de vehículos registrados, retirados y en parqueo.
- Ver total pagado.
- Ver tiempo promedio de parqueo.
- Ver lista de usuarios.
- Ver vehículo con más y menos tiempo en el parqueadero.

## Archivos exportados

| Archivo                         | Contenido                                  |
|--------------------------------|--------------------------------------------|
| `usuarios.csv`                 | Lista de usuarios registrados              |
| `vehiculos_retirados.csv`      | Datos de retiro y cobro                    |
| `informe_vehiculos_retirados.csv` | Informe completo con nombre, tiempos y pago |
| `log_eventos.txt`              | Registro de operaciones realizadas         |

---

## Consejos de uso

- Puedes cerrar sesión en cualquier momento usando la opción 5 del menú.
- Si cometes un error al ingresar datos, el sistema te guiará para corregirlos.
- El sistema funciona en cualquier terminal o consola que soporte Python 3.

---

## Desarrollado por

Estudiantes de Ingeniería Industrial  
Esneider Montes hincapie / Valeria Henao Londono
Universidad de Antioquia – Facultad de Ingeniería  
2025-1
