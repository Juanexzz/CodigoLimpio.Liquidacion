import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from model import liquidacion_total
from controller.liquidaciones_controller import LiquidacionesController
from model.empleado_liquidacion import EmpleadoLiquidacion

def obtener_datos_empleado():
    salario_auxilio = float(input("Ingrese el salario con auxilio: "))
    salario_sin_auxilio = float(input("Ingrese el salario sin auxilio: "))
    salario_variable = float(input("Ingrese el salario variable: "))
    fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/yyyy): ")
    fecha_fin = input("Ingrese la fecha de fin (dd/mm/yyyy): ")
    dias_suspension = int(input("Ingrese los días de suspensión: "))
    dias_indemnizacion = int(input("Ingrese los días de indemnización: "))
    
    return salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion

def mostrar_resultados(liquidacion):
    print("\n=== Resultados de la Liquidación ===")
    print(f"Prima: {liquidacion.calcular_prima():.2f}")
    print(f"Cesantías: {liquidacion.calcular_cesantias():.2f}")
    print(f"Intereses sobre cesantías: {liquidacion.calcular_intereses_cesantias():.2f}")
    print(f"Vacaciones: {liquidacion.calcular_vacaciones():.2f}")
    print(f"Indemnización: {liquidacion.calcular_indemnizacion():.2f}")
    print(f"Total liquidación: {liquidacion.calcular_liquidacion_total():.2f}")

def main():
    while True:
        print("\n1. Calcular e Insertar Liquidación")
        print("2. Modificar Liquidación por ID")
        print("3. Buscar Liquidación por ID")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                datos = obtener_datos_empleado()
                liquidacion = liquidacion_total.LiquidacionEmpleado(*datos)
                mostrar_resultados(liquidacion)

                # Insertar en base de datos
                empleado = EmpleadoLiquidacion(*datos)
                id_insertado = LiquidacionesController.insertar(empleado)
                print(f"\nLiquidación insertada con ID: {id_insertado}")

            except liquidacion_total.ErrorLiquidacion as e:
                print(f"Error: {e}")

        elif opcion == "2":
            try:
                id_modificar = int(input("Ingrese el ID de la liquidación a modificar: "))
                datos = obtener_datos_empleado()
                nuevo_empleado = EmpleadoLiquidacion(*datos)
                LiquidacionesController.modificar_por_id(id_modificar, nuevo_empleado)
                print(f"Liquidación con ID {id_modificar} modificada correctamente.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            id_buscar = int(input("Ingrese el ID de la liquidación a buscar: "))
            empleado = LiquidacionesController.buscar_por_id(id_buscar)
            if empleado:
                print(f"\n=== Datos del empleado con ID {id_buscar} ===")
                liquidacion = liquidacion_total.LiquidacionEmpleado(
                    empleado.salario_auxilio,
                    empleado.salario_sin_auxilio,
                    empleado.salario_variable,
                    empleado.fecha_inicio,
                    empleado.fecha_fin,
                    empleado.dias_suspension,
                    empleado.dias_indemnizacion
                )
                print(liquidacion)
            else:
                print("No se encontró la liquidación con ese ID.")


        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()