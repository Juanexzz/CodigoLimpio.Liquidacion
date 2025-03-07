from datetime import datetime

# Definición de una excepción personalizada para errores en la liquidación
class ErrorLiquidacion(Exception):
    ...

# Constantes del sistema para cálculos de liquidación
salario_minimo = 1300000
dias_laborales = 30
dias_anio = 360
dias_vacaciones_anual = 15
porcentaje_intereses = 0.12

class LiquidacionEmpleado:
    def __init__(self, salario_auxilio, salario_sin_auxilio, salario_variable, 
                 fecha_inicio_contrato, fecha_fin_contrato, dias_suspension, dias_indemnizacion):
        
        # Validación del salario base
        if salario_sin_auxilio < salario_minimo:
            raise ErrorLiquidacion("El salario sin auxilio debe ser mayor o igual a 1,300,000")
        
        # Validación del salario variable
        if salario_variable < 0:
            raise ErrorLiquidacion("El salario variable no puede ser negativo")
        
        # Validación y conversión de fechas
        try:
            self.fecha_inicio_contrato = datetime.strptime(fecha_inicio_contrato, "%d/%m/%Y")
            self.fecha_fin_contrato = datetime.strptime(fecha_fin_contrato, "%d/%m/%Y")
        except ValueError:
            raise ErrorLiquidacion("El formato de la fecha debe ser dd/mm/yyyy")
        
        # Validación de coherencia de fechas
        if self.fecha_inicio_contrato > self.fecha_fin_contrato:
            raise ErrorLiquidacion("La fecha de inicio no puede ser posterior a la fecha de fin")

        # Asignación de atributos con ajustes necesarios
        self.salario_auxilio = salario_auxilio + salario_variable  # Se suma el salario variable
        self.salario_sin_auxilio = salario_sin_auxilio
        self.dias_trabajados = max((self.fecha_fin_contrato - self.fecha_inicio_contrato).days - dias_suspension, 0)  # Se restan días de suspensión
        self.salario_diario = salario_sin_auxilio / dias_laborales
        self.dias_indemnizacion = dias_indemnizacion

    def calcular_prima(self):
        """ Calcula la prima de servicios basada en los días trabajados. """
        return round(self.salario_auxilio * self.dias_trabajados / dias_anio, 0)

    def calcular_cesantias(self):
        """ Calcula las cesantías acumuladas en función de los días trabajados. """
        return round(self.salario_auxilio * self.dias_trabajados / dias_anio, 0)

    def calcular_intereses_cesantias(self):
        """ Calcula los intereses sobre cesantías. """
        cesantias = self.calcular_cesantias()
        return round(cesantias * porcentaje_intereses * self.dias_trabajados / dias_anio, 0)

    def calcular_vacaciones(self):
        """ Calcula el valor de las vacaciones proporcionales. """
        dias_vacaciones = self.dias_trabajados * dias_vacaciones_anual / dias_anio
        return round(dias_vacaciones * self.salario_diario, 0)

    def calcular_indemnizacion(self):
        """ Calcula la indemnización en función de los días establecidos. """
        return round(self.salario_sin_auxilio / dias_laborales * self.dias_indemnizacion, 0)

    def calcular_liquidacion_total(self):
        """ Calcula el monto total de la liquidación sumando todos los conceptos. """
        total = (self.calcular_prima() + self.calcular_cesantias() +
                 self.calcular_intereses_cesantias() + self.calcular_vacaciones() +
                 self.calcular_indemnizacion()) 
        return round(total, 0)

