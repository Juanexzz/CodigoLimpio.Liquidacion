# CodigoLimpio.Liquidacion📊 Sistema de Liquidación de Nómina

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 👥 Contribuidores

- Miguel Guarnizo [github.com/Miguel-Angel-Salazar](https://github.com/Miguel-Angel-Salazar)
- Miguel Salas [github.com/Emblask](https://github.com/Emblask)

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
    │   │    └── kivy.py                (Vacío por ahora)
    │   └── web/ 
    │        └── app.py                 (Vacío por ahora)
    ├── controller/
    │   ├── __init__.py
    │   ├── liquidaciones_controller.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test.py                     Contiene pruebas del sistema
    │   └── test_sql.py                 Pruebas y creación de tablas SQL
    ├── README.md                       Este archivo
    ├── casos de prueba codigo_limpio1.0.xlsx   Casos de prueba
    ├── Experto.mp3                     Audio guía
    └── secretconfig.py                Configuración local de base de datos (NO incluir en Git)
```

---

## 📄 Licencia

MIT License
