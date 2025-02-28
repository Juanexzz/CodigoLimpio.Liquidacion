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
    │   └── liquidacion_total.py  # Lógica principal
    │	└── consola.py 		  #logica para imprimir por consola	
    ├── tests/
    │   └── test_liquidacion.py   # Pruebas unitarias
    └── README.md                 # Documentación
```

## 📄 Licencia

MIT License

## 👥 Contribuidores

- Miguel Guarnizo github.com/Miguel-Angel-Salazar
- Miguel Salas github.com/Emblask
	
