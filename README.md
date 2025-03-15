# CodigoLimpio.Liquidacion📊 Sistema de Liquidación de Nómina

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 👥 Contribuidores

- Miguel Guarnizo github.com/Miguel-Angel-Salazar
- Miguel Salas github.com/Emblask

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

1. Clona el repositorio
	git clone ```https://github.com/Emblask/CodigoLimpio.Liquidacion.git```
   
2. Requisitos:
        Python 3.8+

## ⌨️ Uso Interfaz por Consola

1. Por medio de la consola, Ubicados en la carpeta raiz del proyecto \CodigoLimpio.Liquidacion
2. ejecutar el siguiente comando:
   - python src/view/console/main.py




## 🛠️ Uso de los tests
1. Por medio de la consola, Ubicados en la carpeta raiz del proyecto \CodigoLimpio.Liquidacion
2. Ejecutar el siguiente comando:
   - python tests/test.py
   
---

## 🔍 Entradas
1. Sueldo
2. Sueldo con Auxilio
3. Fecha de ingreso
4. Fecha de retiro
5. Salario Variable
6. Dias de suspencion
7. Dias de indemnizacion

## ⚙️ Procesos
- Este proceso consiste en calcular la liquidación final de una persona (empleado) cuando termina su vínculo laboral, así como las prestaciones sociales que le corresponden según la normativa vigente.
  
## 📤 Salidas
1. Valor de Prima
2. Valor de Cesantias
3. Valor de intereses de cesantias
4. Valor de Vacaciones
5. Total Liquidacion

--- 
## 🗂️ Estructura del Proyecto
```
└── src/
    ├── model/
    │   ├──  liquidacion_total.py		Es el archivo base del proyecto, que contiene la logica para calcular la liquidacíon total
    │	└── __init__.py	
    ├── view/
    │	├── console/
    │	│    └── main.py			Archivo por el cual se corre por consola el programa
    │	├── gui/
    │	│    └── kivy.py			Archivo vacio de momento
    │	└── web/ 
    │	     └── app.py				Archivo vacio de momento
    ├── controller/
    │	├── __init__.py
    │	├── urls.py				Archivo vacio de momento
    │	└── blueprints.py			Archivo vacio de momento
    ├── tests
    │	├── __init__.py
    │	└── test.py				Archivo que contiene los 10 tests realizados al programa
    ├──	README.md                		README.md actual con información respecto al codigo
    ├── casos de prueba codigo_limpio1.0.xlsx	Excel con información de los casos de prueba
    ├── Experto.mp3				Audio del experto que nos guió en el proceso de calcular la liquidación total
    └── config.py				Archivo vacio de momento
```

## 📄 Licencia

MIT License


	
