# CodigoLimpio.Liquidacion📊 Sistema de Liquidación de Nómina

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 👥 Contribuidores

- Miguel Guarnizo [github.com/Miguel-Angel-Salazar](https://github.com/Miguel-Angel-Salazar)
- Miguel Salas [github.com/Emblask](https://github.com/Emblask)

---


## 👥 Colaboradores

- Juan Esteban Vallejo Hincapie
- Santiago Restrepo Fonnegra

---


Un sistema para calcular la liquidación laboral de empleados según la normativa colombiana, incluyendo prestaciones sociales, indemnizaciones y otros conceptos.

## 🚀 Características

- **Cálculo automático** de:
  - Prima de servicios
  - Cesantías
  - Intereses sobre cesantías
  - Vacaciones
  - Indemnizaciones
  - Liquidación total
- Validación de fechas y parámetros
- Pruebas unitarias integradas

---

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Emblask/CodigoLimpio.Liquidacion.git
   ```

2. Requisitos:
   - Python 3.8+

---

## 🌐 Acceso en Línea

Puedes usar la aplicación directamente desde la web sin necesidad de instalación:
🔗 https://codigolimpio-liquidacion.onrender.com

Cuando presiones Borrar Tabla de Liquidaciones, inmediatamente dale al boton Crear tabla de liquidaciones para evitar errores

---

## ⚙️ Configuración para funcionalidad SQL

Para que la funcionalidad de base de datos funcione correctamente:

1. **llena el archivo `secretconfig.py`** con los siguientes datos:

   ```python
	PGHOST='ingrese nombre del host'
	PGDATABASE='ingrese nommbre de la base de datos'
	PGUSER='ingrese nombre de usuario'
	PGPASSWORD='ingrese contraseña'
   ```

2. **Ejecuta los tests SQL** desde la carpeta raíz del proyecto para crear las tablas necesarias:

   ```bash
   python -m unittest tests/test_sql.py
   ```

---
## Ejecución Local web

Para ejecutar la aplicación en tu entorno local:

1.  Abre tu terminal o símbolo del sistema.
2.  Navega hasta el directorio raíz del proyecto (donde se encuentra el archivo `app.py`).
3.  Ejecuta el siguiente comando:
    ```bash
    python app.py
    ```
4.  Una vez que el servidor de Flask se inicie, podrás acceder a la aplicación abriendo tu navegador web y dirigiéndote a la siguiente dirección:
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```

## Configuración de la Base de Datos (Para una Base de Datos Vacía)

Estos pasos te guiarán para conectar la aplicación a una base de datos PostgreSQL vacía y configurar las tablas necesarias:

1.  **Requisitos Previos:**
    * Asegúrate de tener PostgreSQL instalado y en ejecución en tu sistema.
    * Crea una base de datos vacía en PostgreSQL que utilizarás para este proyecto.

2.  **Configuración de las Credenciales:**
    * Localiza el archivo `secretconfig.py` en la raíz del proyecto.
    * Edita este archivo con los detalles de conexión a tu base de datos PostgreSQL. Reemplaza los valores placeholder con tu información real:
        ```python
        PGHOST='tu_nombre_de_host'
        PGDATABASE='el_nombre_de_tu_base_de_datos'
        PGUSER='tu_nombre_de_usuario'
        PGPASSWORD='tu_contraseña'
        ```
        Guarda los cambios en `secretconfig.py`.

3.  **Creación de las Tablas:**
    * Desde la raíz del proyecto (la misma ubicación donde está `app.py`), ejecuta el siguiente comando para correr los tests SQL. Estos tests están diseñados para crear las tablas necesarias en la base de datos configurada:
        ```bash
        python -m unittest tests/test_sql.py
        ```

    Tras completar estos pasos, tu aplicación debería estar conectada a la base de datos y las tablas necesarias deberían haber sido creadas.

## ⌨️ Uso Interfaz por Consola

1. Desde la carpeta raíz del proyecto `CodigoLimpio.Liquidacion`
2. Ejecuta el siguiente comando:
   ```bash
   python src/view/console/main.py
   ```

---

## 🛠️ Uso de los tests

1. Desde la carpeta raíz del proyecto:
   ```bash
   python tests/test.py
   ```

---

## 🔍 Entradas
1. Sueldo
2. Sueldo con Auxilio
3. Fecha de ingreso
4. Fecha de retiro
5. Salario Variable
6. Días de suspensión
7. Días de indemnización

## ⚙️ Procesos
- Este proceso consiste en calcular la liquidación final de una persona (empleado) cuando termina su vínculo laboral, así como las prestaciones sociales que le corresponden según la normativa vigente.
  
## 📤 Salidas
1. Valor de Prima
2. Valor de Cesantías
3. Valor de intereses de cesantías
4. Valor de Vacaciones
5. Total Liquidación

---

## 🗂️ Estructura del Proyecto
```
└── src/
    ├── model/
    │   ├── liquidacion_total.py        Lógica principal para el cálculo de la liquidación
    │   ├── empleado_liquidacion.py
    │   └── __init__.py    
    ├── view/
    │   ├── console/
    │   │    └── main.py                Ejecutable de consola
    │   ├── gui/
    │   │    └── Main_screen.py
	│    └──Second_screen.py
	│    └──kivy_liquidador.py
        │    └──own_classes.py              
    │   └── web/
    │        └── templates
    │        └── plano.py
             └── requirements.txt          
    ├── controller/
    │   ├── __init__.py
    │   ├── liquidaciones_controller.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test.py                     Contiene pruebas del sistema
    │   └── test_sql.py                 Pruebas y creación de tablas SQL
    ├── app.py  
    ├── README.md                       Este archivo
    ├── casos de prueba codigo_limpio1.0.xlsx   Casos de prueba
    ├── Experto.mp3                     Audio guía
    └── secretconfig.py                Configuración local de base de datos (NO incluir en Git)
```

---

## 📄 Licencia

MIT License
