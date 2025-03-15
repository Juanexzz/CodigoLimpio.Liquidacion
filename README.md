# CodigoLimpio.Liquidacion📊 Sistema de Liquidación de Nómina

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Un sistema para calcular la liquidación laboral de empleados según la normativa colombiana, incluyendo prestaciones sociales, indemnizaciones y otros conceptos.

---

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

1. Acceder a la terminal de VS Code, lo puedes de hacer de forma manual o con el atajo
   Ctrl + Ñ (Windows/Linux) o Cmd + Ñ (Mac)

2. Vas a poner lo siguiente:
   - cd src/view/console
   - python main.py
     
"Con esto ya tendras acceso a la consola."

3. Para que veas su funcionamientos, te recomendamos usar uno de nuestros casos pruba.


## 🛠️ Uso
1. Ejecutar tests python -m unittest test/test_logic.py
2. Ejecutar codigo
	
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


## 🗂️ Estructura del Proyecto
```
└── src/
    ├── model/
    │   ├──  liquidacion_total.py
    │	└── __init__.py	
    ├── view/
    │	├── console/
    │	│    └── main.py
    │	├── gui/
    │	│    └── kivy.py
    │	└── web/ 
    │	     └── app.py
    ├── controller/
    │	├── __init__.py
    │	├── urls.py
    │	└── blueprints.py
    ├── README.md                
    ├── casos de prueba codigo_limpio1.0.xlsx
    ├── Experto.mp3
    ├── config.py
    └── test.py
```

## 📄 Licencia

MIT License

## 👥 Contribuidores

- Miguel Guarnizo github.com/Miguel-Angel-Salazar
- Miguel Salas github.com/Emblask
	
