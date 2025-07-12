# Project_Alg-Prom

## ACTAS
### Acta de colaboración
[Acta de Colaboración.pdf](https://github.com/user-attachments/files/20020686/Acta.de.Colaboracion.pdf)

### Acta de entendimiento
[Acta de Entendimiento.pdf](https://github.com/user-attachments/files/20020688/Acta.de.Entendimiento.pdf)

### Acta de responsabilidad
[Acta de Responsabilidad.pdf](https://github.com/user-attachments/files/20020689/Acta.de.Responsabilidad.pdf)

# ENTREGABLE (1ra ENTREGA, 1 - 7)

## S.I.P.U - SISTEMA INTEGRAL DEL PARQUEO URBANO

### 1) Integrantes y Descripcion
Esneider Montes Hincapie - Valeria Henao Londoño

Este repositorio corresponde a nuestro proyecto final para el curso de Algoritmia y Programación de la Universidad de Antioquia. El proyecto está enfocado en la creación de un sistema de gestión para el parqueadero universitario **Parking Trust**.

### 2) Vinculos academicos y descripcion 
#### Esneider Hincapie
**Programa:** Ingenieria Industrial  

**Habilidades y Fortalezas:**  
- Análisis de datos  
- Contabilidad y finanzas  
- Manejo de Excel  
- Inglés básico  
- Trabajo en equipo  
- Adaptabilidad  
- Gestión del tiempo  
- Empatía  
- Resolución de problemas  

**Descripción:**
Esneider aporta una base sólida en gestión financiera, análisis de información y organización, lo cual fortalece el control y seguimiento técnico del sistema.

#### Valeria Henao Londoño  
**Programa:** Ingenieria Industrial  

**Habilidades y Fortalezas:**  
- Perseverancia  
- Capacidad para negociar sin parecer agresiva  
- Resolución de conflictos sin escalar los problemas  
- Habilidad para pedir ayuda en el momento y a la persona correcta  

**Descripción:**  
Valeria contribuye al equipo con habilidades interpersonales clave para la coordinación del proyecto, comunicación efectiva y resolución de situaciones críticas de forma equilibrada.

### 3. Nombre del Proyecto y Detalles
**Nombre del proyecto:** S.I.P.U – Sistema Integral del Parqueo Urbano

![S I P U](https://github.com/user-attachments/assets/bd75d302-eed4-4d88-b30f-b31504d69a01)

**Descripción del proyecto:**  
S.I.P.U es una aplicación de consola desarrollada en Python que busca gestionar el parqueadero universitario **Parking Trust**, permitiendo registrar usuarios, controlar el ingreso y retiro de vehículos, calcular tarifas de parqueo y generar reportes administrativos. Todo esto con una interfaz amigable y exportación de datos en formato CSV.

### 4) licencia del software 
**S.I.P.U © 2025 by ESNEIDER MONTES HINCAPIE & VALERIA HENAO LONDOÑO is licensed under CC BY-NC-ND 4.0**

### 5) reporte de vision
#### El sistema cubrira:
  * Registro y validacion de datos de usuarios y vehiculos.
  * Control de ingreso y salida de vehiculos.
  * Calculo y cobro de tarifas segun tiempo.
  * Acceso a un módulo administrativo protegido por credenciales.
  * Exportacion de reportes a CSV.
  
#### Objetivo:
  Desarrollar un software de consola amigable para gestionar el parqueadero universitario, automatizando el registro, cobro y reporte de vehículos.

#### Beneficios:
  * Mejora la organización y trazabilidad del parqueadero.
  * Reduce errores humanos.
  * Facilita el análisis administrativo con reportes exportables.

### 6) especificacion de requisitos 
#### Requisitos funcionales
  * Registrar usuarios con validaciones estrictas (nombre, apellido, documento, placa).
  * Ingreso de vehículos de usuarios registrados.
  * Registro de hora de entrada y salida.
  * Cálculo automático del cobro.
  * Generación de factura en consola.
  * Exportación de reportes a archivo CSV.
  * Acceso administrativo con usuario y contraseña.
  * Reportes: vehículos registrados, retirados, sin retirar, pagos, tiempo promedio, etc.
  * Registro de logs de eventos con precisión temporal.

#### Requisitos no funcionales
  * Interfaz de consola amigable y validada.
  * Tiempo de respuesta rápido (< 1 segundo en operaciones básicas).
  * Código estructurado y documentado.
  * Uso de estructuras de datos eficientes.

### 7. Plan de Proyecto

#### Actividades del Proyecto
1. Reunión inicial y acta de entendimiento
2. Levantamiento de requisitos con el Product Owner (profesor)
3. Diseño del modelo lógico y estructura de datos
4. Desarrollo del módulo de registro de usuarios
5. Desarrollo del módulo de ingreso y retiro de vehículos
6. Desarrollo del módulo administrativo y generación de reportes
7. Pruebas funcionales y de validación de datos
8. Exportación de reportes a formato CSV
9. Documentación técnica y manual de usuario
10. Presentación final y sustentación del proyecto

#### Cronograma General (tipo Gantt - Semana 1 a 16)

| Semana | Actividad                                                     |
|--------|---------------------------------------------------------------|
| 1      | Reunión inicial y actas                                       |
| 2 - 3  | Recolección de requisitos y diseño general del sistema        |
| 4 - 6  | Desarrollo de funcionalidades principales                     |
| 7 - 8  | Pruebas iniciales y entrega parcial (puntos 1 al 7)           |
| 9 - 12 | Desarrollo del módulo administrativo y exportación de datos   |
| 13 - 14| Documentación y pruebas finales                               |
| 15     | Preparación de sustentación                                   |
| 16     | Sustentación del proyecto                                     |

#### Presupuesto del Proyecto
El desarrollo del proyecto se calcula con base en **tiempo de práctica formativa**. Nuestro equipo está conformado por **2 estudiantes**, con una dedicación total estimada de **50 horas** (25 horas por estudiante).

- Valor de referencia: **1 SMMLV mensual en Colombia**.
- Suposición: 1 SMLV = **$1.423.500 COP**
- Valor hora de práctica:  
  $1.423.500 / 160 horas mensuales ≈ **$8.896,87 COP/hora**
- Costo total del proyecto:  
  50 horas × $8.896,87 = **$444.853,75 COP (equivalente en tiempo invertido)**

*(**Nota**: Este valor es simbólico y representa el tiempo invertido como práctica formativa, no un cobro monetario.)*

#### Plan de Versionado - Parking Trust

A continuación se describe el historial de versiones del software "Parking Trust".

| Versión | Fecha       | Descripción                                                     |
|--------:|-------------|-----------------------------------------------------------------|
| 0.1     | 2025-04-28  | Inicio del proyecto. Se define la estructura y requisitos.     |
| 0.2     | 2025-05-15  | Se desarrolla el registro de usuarios y validaciones.          |
| 0.3     | 2025-05-26  | Implementación del ingreso de vehículos y gestión de parqueo.  |
| 0.4     | 2025-06-03  | Módulo de retiro de vehículos y cálculo de tarifas.            |
| 0.5     | 2025-07-01  | Submenú administrador con reportes y estadísticas.             |
| 1.0     | 2025-07-12  | Versión final: exportación CSV, login, y documentación completa.|

#### Código fuente carpeta src

El código principal del proyecto se encuentra en la carpeta [`src`](./src):

- [`parking_trust.py`](./src/parking_trust.py): contiene todo el algoritmo funcional del sistema Parking Trust, desde el registro hasta los reportes administrativos y la exportación de datos.

