from datetime import datetime

class LiquidacionEmpleado:
    def __init__(self, salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion):
        self.salario_auxilio = salario_auxilio + salario_variable  # Se suma el salario variable
        self.salario_sin_auxilio = salario_sin_auxilio
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        self.fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        self.dias_trabajados = max((self.fecha_fin - self.fecha_inicio).days - dias_suspension, 0)  # Se restan días de suspensión
        self.salario_diario = salario_sin_auxilio / 30
        self.dias_indemnizacion = dias_indemnizacion

    def calcular_prima(self):
        return round(self.salario_auxilio * self.dias_trabajados / 360, 0)

    def calcular_cesantias(self):
        return round(self.salario_auxilio * self.dias_trabajados / 360, 0)

    def calcular_intereses_cesantias(self):
        cesantias = self.calcular_cesantias()
        return round(cesantias * 0.12 * self.dias_trabajados / 360, 0)

    def calcular_vacaciones(self):
        dias_vacaciones = self.dias_trabajados * 15 / 360
        return round(dias_vacaciones * self.salario_diario, 0)

    def calcular_indemnizacion(self):
        return round(self.salario_sin_auxilio / 30 * self.dias_indemnizacion, 0)

    def calcular_liquidacion_total(self):
        total = (self.calcular_prima() + self.calcular_cesantias() +
                 self.calcular_intereses_cesantias() + self.calcular_vacaciones() +
                 self.calcular_indemnizacion())  # Se suma la indemnización
        return round(total, 0)

def obtener_datos():
    datos = {
        "salario_auxilio": 1462000, 
        "salario_sin_auxilio": 1300000, 
        "salario_variable": 200000,  # Ejemplo de salario variable
        "fecha_inicio": "01/02/2024",
        "fecha_fin": "30/06/2024",
        "dias_suspension": 5,  # Ejemplo de días de suspensión
        "dias_indemnizacion": 10  # Ejemplo de días de indemnización
    }
    return datos

datos = obtener_datos()

empleado = LiquidacionEmpleado(
    datos["salario_auxilio"], datos["salario_sin_auxilio"], datos["salario_variable"],
    datos["fecha_inicio"], datos["fecha_fin"], datos["dias_suspension"], datos["dias_indemnizacion"]
)

print(f"Días trabajados: {empleado.dias_trabajados}")
print(f"Prima: ${empleado.calcular_prima():,.0f}")
print(f"Vacaciones: ${empleado.calcular_vacaciones():,.0f}")
print(f"Cesantías: ${empleado.calcular_cesantias():,.0f}")
print(f"Intereses cesantías: ${empleado.calcular_intereses_cesantias():,.0f}")
print(f"Indemnización: ${empleado.calcular_indemnizacion():,.0f}")
print(f"Total liquidación: ${empleado.calcular_liquidacion_total():,.0f}")