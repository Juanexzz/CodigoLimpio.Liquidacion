import unittest
import sys
sys.path.append("src")
from model.liquidacion_total import LiquidacionEmpleado as Liquidacion

class TestContractDetails(unittest.TestCase):

    def test_normal_1(self):
        # Variables de entrada
        fecha_inicio = "01/02/2024"
        fecha_fin = "30/06/2024"
        salario_auxilio = 1462000
        salario_sin_auxilio = 1300000
        dias_suspension = 0
        dias_indemnizacion = 0
        salario_variable = 0

        # Resultado esperado (corregido)
        prima = 609167
        vacaciones = 270833
        cesantias = 609167
        intereses_cesantias = 30458
        liquidacion_total = 1519625

        # Proceso
        Mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)
        prima_resultados = Mi_liquidacion.calcular_prima()
        vacaciones_resultados = Mi_liquidacion.calcular_vacaciones()
        cesantias_resultados = Mi_liquidacion.calcular_cesantias()
        intereses_cesantias_resultados = Mi_liquidacion.calcular_intereses_cesantias()
        liquidacion_total_resultados = Mi_liquidacion.calcular_liquidacion_total()

        # Verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    # Resto de las pruebas...

    
    def test_normal_2(self):
        
        #variables de entrada 
        fecha_inicio = "01/01/2024"
        fecha_fin = "20/12/2024"
        salario_auxilio = 1662000
        salario_sin_auxilio = 1500000
        dias_suspension = 0
        dias_indemnizacion =0
        salario_variable = 0

        #resultado esperado
        prima =  784333
        vacaciones = 729167
        cesantias = 1615833
        intereses_cesantias = 188514
        liquidacion_total = 3585347

        #proceso
        Mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)
        prima_resultados = Mi_liquidacion.calcular_prima()
        vacaciones_resultados = Mi_liquidacion.calcular_vacaciones()
        cesantias_resultados = Mi_liquidacion.calcular_cesantias()
        intereses_cesantias_resultados = Mi_liquidacion.calcular_intereses_cesantias()
        liquidacion_total_resultados = Mi_liquidacion.calcular_liquidacion_total()
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    def test_normal_3(self):
        
        #variables de entrada 
        fecha_inicio = "01/07/2024"
        fecha_fin = "30/10/2024"
        salario_auxilio =  3662000 
        salario_sin_auxilio = 3500000
        dias_suspension = 0
        dias_indemnizacion =0
        salario_variable = 0

        #resultado esperado
        prima = 1223445
        vacaciones = 583333 
        cesantias = 1222048
        intereses_cesantias = 48882
        liquidacion_total = 3077708  

        #proceso
        Mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)
        prima_resultados = Mi_liquidacion.calcular_prima()
        vacaciones_resultados = Mi_liquidacion.calcular_vacaciones()
        cesantias_resultados = Mi_liquidacion.calcular_cesantias()
        intereses_cesantias_resultados = Mi_liquidacion.calcular_intereses_cesantias()
        liquidacion_total_resultados = Mi_liquidacion.calcular_liquidacion_total()
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    def test_extraordinario_1(self):
        
        #variables de entrada 
        fecha_inicio = "01/01/2021"
        fecha_fin = "30/12/2024"
        salario_auxilio =  1462000 
        salario_sin_auxilio = 1300000
        dias_suspension = 0
        dias_indemnizacion =0
        salario_variable = 50000

        #resultado esperado
        prima = 2600000
        vacaciones = 2600000  
        cesantias = 5200000
        intereses_cesantias = 624000
        liquidacion_total = 14924000
          

        #proceso
        Mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)
        prima_resultados = Mi_liquidacion.calcular_prima()
        vacaciones_resultados = Mi_liquidacion.calcular_vacaciones()
        cesantias_resultados = Mi_liquidacion.calcular_cesantias()
        intereses_cesantias_resultados = Mi_liquidacion.calcular_intereses_cesantias()
        liquidacion_total_resultados = Mi_liquidacion.calcular_liquidacion_total()
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    def test_extraordinario_2(self):
        
        #variables de entrada 
        fecha_inicio = "16/01/2024"
        fecha_fin = "21/12/2024"
        salario_auxilio =  1462000 
        salario_sin_auxilio = 1300000
        dias_suspension = 5
        dias_indemnizacion =0
        salario_variable = 0

        #resultado esperado
        prima = 678206
        vacaciones = 597639  
        cesantias = 1396756
        intereses_cesantias = 154109
        liquidacion_total = 2420104 

        #proceso
        Mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)
        prima_resultados = Mi_liquidacion.calcular_prima()
        vacaciones_resultados = Mi_liquidacion.calcular_vacaciones()
        cesantias_resultados = Mi_liquidacion.calcular_cesantias()
        intereses_cesantias_resultados = Mi_liquidacion.calcular_intereses_cesantias()
        liquidacion_total_resultados = Mi_liquidacion.calcular_liquidacion_total()
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)

    def test_extraordinario_3(self):
        
        #variables de entrada 
        fecha_inicio = "01/01/2024"
        fecha_fin = "20/12/2024"
        salario_auxilio =  1762000 
        salario_sin_auxilio = 1600000
        dias_suspension = 0
        dias_indemnizacion = 50
        salario_variable = 0

        #resultado esperado
        prima = 865015
        vacaciones = 695833 
        cesantias = 1622961
        intereses_cesantias = 162837
        liquidacion_total = 3397114 

        #proceso
        Mi_liquidacion = Liquidacion(salario_auxilio, salario_sin_auxilio, salario_variable, fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion)
        prima_resultados = Mi_liquidacion.calcular_prima()
        vacaciones_resultados = Mi_liquidacion.calcular_vacaciones()
        cesantias_resultados = Mi_liquidacion.calcular_cesantias()
        intereses_cesantias_resultados = Mi_liquidacion.calcular_intereses_cesantias()
        liquidacion_total_resultados = Mi_liquidacion.calcular_liquidacion_total()
        

        #verificación
        self.assertEqual(prima, prima_resultados)
        self.assertEqual(vacaciones, vacaciones_resultados)
        self.assertEqual(cesantias, cesantias_resultados)
        self.assertEqual(intereses_cesantias, intereses_cesantias_resultados)
        self.assertEqual(liquidacion_total, liquidacion_total_resultados)


if __name__ == '__main__':
    unittest.main()
