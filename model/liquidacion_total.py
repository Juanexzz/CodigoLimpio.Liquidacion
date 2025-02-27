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
                 self.calcular_indemnizacion()) 
        return round(total, 0)