from datetime import datetime

class EmpleadoLiquidacion:
    """
    Pertenece a la Capa de Reglas de Negocio (Model)

    Representa los datos necesarios para calcular la liquidación de un empleado
    """

    def __init__(self, salario_auxilio, salario_sin_auxilio, salario_variable,
                 fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion):
        
        self.salario_auxilio = salario_auxilio
        self.salario_sin_auxilio = salario_sin_auxilio
        self.salario_variable = salario_variable
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        self.fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        self.dias_suspension = dias_suspension
        self.dias_indemnizacion = dias_indemnizacion

    def esIgual(self, comparar_con):
        """
        Compara el objeto actual con otra instancia de EmpleadoLiquidacion
        """
        assert self.salario_auxilio == comparar_con.salario_auxilio
        assert self.salario_sin_auxilio == comparar_con.salario_sin_auxilio
        assert self.salario_variable == comparar_con.salario_variable
        assert self.fecha_inicio == comparar_con.fecha_inicio
        assert self.fecha_fin == comparar_con.fecha_fin
        assert self.dias_suspension == comparar_con.dias_suspension
        assert self.dias_indemnizacion == comparar_con.dias_indemnizacion
        return True
    
    def __str__(self):
        return (
            f"Salario con auxilio: {self.salario_auxilio}\n"
            f"Salario sin auxilio: {self.salario_sin_auxilio}\n"
            f"Salario variable: {self.salario_variable}\n"
            f"Fecha de inicio: {self.fecha_inicio.strftime('%d/%m/%Y')}\n"
            f"Fecha de fin: {self.fecha_fin.strftime('%d/%m/%Y')}\n"
            f"Días de suspensión: {self.dias_suspension}\n"
            f"Días de indemnización: {self.dias_indemnizacion}"
        )
    
