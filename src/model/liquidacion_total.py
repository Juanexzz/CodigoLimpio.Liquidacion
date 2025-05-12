from datetime import datetime

salario_minimo = 1300000
dias_al_mes = 30
dias_al_año = 360
porcentaje_interes = 0.12
dias_de_vacaciones = 15

class ErrorLiquidacion (Exception):
    ...


class LiquidacionEmpleado:
    def __init__(self, salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion):
        self.salario_auxilio = salario_auxilio
        self.salario_sin_auxilio = salario_sin_auxilio
        self.salario_variable = salario_variable

        # Verificar si fecha_inicio es una cadena (str) o un objeto datetime
        if isinstance(fecha_inicio, str):
            self.fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        elif isinstance(fecha_inicio, datetime):
            self.fecha_inicio = fecha_inicio
        else:
            raise ValueError("fecha_inicio debe ser un objeto datetime o una cadena con formato dd/mm/yyyy")

        # Verificar si fecha_fin es una cadena (str) o un objeto datetime
        if isinstance(fecha_fin, str):
            self.fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        elif isinstance(fecha_fin, datetime):
            self.fecha_fin = fecha_fin
        else:
            raise ValueError("fecha_fin debe ser un objeto datetime o una cadena con formato dd/mm/yyyy")

        self.dias_suspension = dias_suspension
        self.dias_indemnizacion = dias_indemnizacion

        # Calcular días trabajados, considerando la suspensión
        self.dias_trabajados = max((self.fecha_fin - self.fecha_inicio).days - self.dias_suspension, 0)

        # Calcular salario diario
        self.salario_diario = self.salario_sin_auxilio / dias_al_mes

    def calcular_prima(self):
        return (self.salario_auxilio * self.dias_trabajados / dias_al_año)

    def calcular_cesantias(self):
        return (self.salario_auxilio * self.dias_trabajados / dias_al_año)

    def calcular_intereses_cesantias(self):
        cesantias = self.calcular_cesantias()
        return (cesantias * porcentaje_interes * self.dias_trabajados / dias_al_año)

    def calcular_vacaciones(self):
        dias_vacaciones = self.dias_trabajados * dias_de_vacaciones / dias_al_año
        return (dias_vacaciones * self.salario_diario)

    def calcular_indemnizacion(self):
        return (self.salario_sin_auxilio / dias_al_mes * self.dias_indemnizacion)

    def calcular_liquidacion_total(self):
        total = (self.calcular_prima() + self.calcular_cesantias() +
                 self.calcular_intereses_cesantias() + self.calcular_vacaciones() +
                 self.calcular_indemnizacion()) 
        return total

    def __str__(self):
        # Aquí mostramos los cálculos, de forma legible
        return (f"Salario con auxilio: {self.salario_auxilio}\n"
                f"Salario sin auxilio: {self.salario_sin_auxilio}\n"
                f"Salario variable: {self.salario_variable}\n"
                f"Fecha de inicio: {self.fecha_inicio.strftime('%d/%m/%Y')}\n"
                f"Fecha de fin: {self.fecha_fin.strftime('%d/%m/%Y')}\n"
                f"Días de suspensión: {self.dias_suspension}\n"
                f"Días de indemnización: {self.dias_indemnizacion}\n"
                f"Prima: {self.calcular_prima()}\n"
                f"Cesantías: {self.calcular_cesantias()}\n"
                f"Intereses de cesantías: {self.calcular_intereses_cesantias()}\n"
                f"Vacaciones: {self.calcular_vacaciones()}\n"
                f"Indemnización: {self.calcular_indemnizacion()}\n"
                f"Total liquidación: {self.calcular_liquidacion_total()}\n")
