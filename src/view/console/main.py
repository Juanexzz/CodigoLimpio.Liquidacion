import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from model import liquidacion_total

try:
    salario_auxilio = float(input("Ingrese el salario con auxilio: "))
    salario_sin_auxilio = float(input("Ingrese el salario sin auxilio: "))
    salario_variable = float(input("Ingrese el salario variable: "))
    fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/yyyy): ")
    fecha_fin = input("Ingrese la fecha de fin (dd/mm/yyyy): ")
    dias_suspension = int(input("Ingrese los días de suspensión: "))
    dias_indemnizacion = int(input("Ingrese los días de indemnización: "))

    liquidacion = liquidacion_total.LiquidacionEmpleado(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)

    print("\n=== Resultados de la Liquidación ===")
    print(f"Prima: {liquidacion.calcular_prima()}")
    print(f"Cesantías: {liquidacion.calcular_cesantias()}")
    print(f"Intereses sobre cesantías: {liquidacion.calcular_intereses_cesantias()}")
    print(f"Vacaciones: {liquidacion.calcular_vacaciones()}")
    print(f"Indemnización: {liquidacion.calcular_indemnizacion()}")
    print(f"Total liquidación: {liquidacion.calcular_liquidacion_total()}")

except liquidacion_total.ErrorLiquidacion as e:
    print(f"Error: {e}")
    