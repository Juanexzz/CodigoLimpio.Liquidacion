from datetime import datetime

class ErrorLiquidacion (Exception):
    ...

class LiquidacionEmpleado:
    def __init__(self, salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion):

        if salario_sin_auxilio < 1300000:
            raise ErrorLiquidacion("Salario incorrecto. El salario sin auxilio debe ser mayor o igual a 1,300,000, por favor ingrese un salario igual o mayor")
        
        if salario_variable < 0:
            raise ErrorLiquidacion("Error de salario variable. El salario variable no puede ser negativo, ingrese un numero mayor que 0")
        
        try:
            self.fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
            self.fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        except ValueError:
            raise ErrorLiquidacion("Error de formato. El formato de la fecha es incorrecto. debe ser dia/mes/año de la siguiente forma dd/mm/yyyy")
        
        if self.fecha_inicio > self.fecha_fin:
            raise ErrorLiquidacion("Fecha incorrecta. La fecha de inicio no puede ser posterior a la fecha de fin. Por favor ingrese fechas validas")

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
