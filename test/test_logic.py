import unittest
import sys
sys.path.append("src")
from model.liquidacion_total import LiquidacionEmpleado as Liquidacion

class TestLiquidacion(unittest.TestCase):

    def test_normal_1(self):
        # Variables de entrada
        fecha_inicio = "01/02/2024"
        fecha_fin = "30/06/2024"
        salario_auxilio = 1462000
        salario_sin_auxilio = 1300000
        dias_suspension = 0
        dias_indemnizacion = 0
        salario_variable = 0

        # Resultados esperados 
        prima = 609167
        vacaciones = 270833
        cesantias = 609167
        intereses_cesantias = 30458
        liquidacion_total = 1519625


        mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)


        self.assertEqual(prima, mi_liquidacion.calcular_prima())
        self.assertEqual(vacaciones, mi_liquidacion.calcular_vacaciones())
        self.assertEqual(cesantias, mi_liquidacion.calcular_cesantias())
        self.assertEqual(intereses_cesantias, mi_liquidacion.calcular_intereses_cesantias())
        self.assertEqual(liquidacion_total, mi_liquidacion.calcular_liquidacion_total())


    def test_normal_2(self):
        # Variables de entrada
        fecha_inicio = "01/01/2024"
        fecha_fin = "20/12/2024"
        salario_auxilio = 1662000
        salario_sin_auxilio = 1500000
        dias_suspension = 0
        dias_indemnizacion = 0
        salario_variable = 0

        # Resultados esperados
        prima = 1634300
        vacaciones = 737500
        cesantias = 1634300
        intereses_cesantias = 192847
        liquidacion_total = 4198947

        mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)


        self.assertEqual(prima, mi_liquidacion.calcular_prima())
        self.assertEqual(vacaciones, mi_liquidacion.calcular_vacaciones())
        self.assertEqual(cesantias, mi_liquidacion.calcular_cesantias())
        self.assertEqual(intereses_cesantias, mi_liquidacion.calcular_intereses_cesantias())
        self.assertEqual(liquidacion_total, mi_liquidacion.calcular_liquidacion_total())

    def test_normal_3(self):
        # Variables de entrada
        fecha_inicio = "01/07/2024"
        fecha_fin = "30/10/2024"
        salario_auxilio = 3662000
        salario_sin_auxilio = 3500000
        dias_suspension = 0
        dias_indemnizacion = 0
        salario_variable = 0

        # Resultados esperados
        prima = 1230839
        vacaciones = 588194
        cesantias = 1230839
        intereses_cesantias = 49644 
        liquidacion_total = 3099516

        mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)


        self.assertEqual(prima, mi_liquidacion.calcular_prima())
        self.assertEqual(vacaciones, mi_liquidacion.calcular_vacaciones())
        self.assertEqual(cesantias, mi_liquidacion.calcular_cesantias())
        self.assertEqual(intereses_cesantias, mi_liquidacion.calcular_intereses_cesantias())
        self.assertEqual(liquidacion_total, mi_liquidacion.calcular_liquidacion_total())

    def test_extraordinario_1(self):
        # Variables de entrada
        fecha_inicio = "01/01/2021"
        fecha_fin = "30/12/2024"
        salario_auxilio = 1462000
        salario_sin_auxilio = 1300000
        dias_suspension = 0
        dias_indemnizacion = 0
        salario_variable = 50000

        # Resultados esperados
        prima = 6127800
        vacaciones = 2634306
        cesantias = 6127800
        intereses_cesantias = 2980153
        liquidacion_total = 17870059

        mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)


        self.assertEqual(prima, mi_liquidacion.calcular_prima())
        self.assertEqual(vacaciones, mi_liquidacion.calcular_vacaciones())
        self.assertEqual(cesantias, mi_liquidacion.calcular_cesantias())
        self.assertEqual(intereses_cesantias, mi_liquidacion.calcular_intereses_cesantias())
        self.assertEqual(liquidacion_total, mi_liquidacion.calcular_liquidacion_total())

    def test_extraordinario_2(self):
        # Variables de entrada
        fecha_inicio = "16/01/2024"
        fecha_fin = "21/12/2024"
        salario_auxilio = 1462000
        salario_sin_auxilio = 1300000
        dias_suspension = 5
        dias_indemnizacion = 0
        salario_variable = 0

        # Resultados esperados 
        prima = 1360472
        vacaciones = 604861
        cesantias = 1360472
        intereses_cesantias = 151919 
        liquidacion_total = 3477724

        mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)


        self.assertEqual(prima, mi_liquidacion.calcular_prima())
        self.assertEqual(vacaciones, mi_liquidacion.calcular_vacaciones())
        self.assertEqual(cesantias, mi_liquidacion.calcular_cesantias())
        self.assertEqual(intereses_cesantias, mi_liquidacion.calcular_intereses_cesantias())
        self.assertEqual(liquidacion_total, mi_liquidacion.calcular_liquidacion_total())

    def test_extraordinario_3(self):
        # Variables de entrada
        fecha_inicio = "01/01/2024"
        fecha_fin = "20/12/2024"
        salario_auxilio = 1762000
        salario_sin_auxilio = 1600000
        dias_suspension = 0
        dias_indemnizacion = 50
        salario_variable = 0

        # Resultados esperados 
        prima = 1732633
        vacaciones = 786667
        cesantias = 1732633 
        intereses_cesantias = 204451
        liquidacion_total = 7123051

        mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)


        self.assertEqual(prima, mi_liquidacion.calcular_prima())
        self.assertEqual(vacaciones, mi_liquidacion.calcular_vacaciones())
        self.assertEqual(cesantias, mi_liquidacion.calcular_cesantias())
        self.assertEqual(intereses_cesantias, mi_liquidacion.calcular_intereses_cesantias())
        self.assertEqual(liquidacion_total, mi_liquidacion.calcular_liquidacion_total())

if __name__ == '__main__':
    unittest.main()