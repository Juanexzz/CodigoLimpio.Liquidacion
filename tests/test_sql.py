import unittest
import sys
sys.path.append("src")

from model.empleado_liquidacion import EmpleadoLiquidacion
from controller.liquidaciones_controller import LiquidacionesController

class TestLiquidacionEmpleado(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        LiquidacionesController.borrar_tabla()
        LiquidacionesController.crear_tabla()

    def test_insert_and_search(self):
        liquidacion = EmpleadoLiquidacion(
            salario_auxilio=1500000,
            salario_sin_auxilio=1300000,
            salario_variable=500000,
            fecha_inicio="01/01/2023",
            fecha_fin="31/12/2023",
            dias_suspension=0,
            dias_indemnizacion=15
        )

        id_insertado = LiquidacionesController.insertar(liquidacion)
        liquidacion_buscada = LiquidacionesController.buscar_por_id(id_insertado)
        self.assertTrue(liquidacion_buscada.esIgual(liquidacion))

    def test_insert_and_search_2(self):
        liquidacion = EmpleadoLiquidacion(
            salario_auxilio=1200000,
            salario_sin_auxilio=1100000,
            salario_variable=400000,
            fecha_inicio="01/06/2023",
            fecha_fin="30/06/2023",
            dias_suspension=0,
            dias_indemnizacion=5
        )

        id_insertado = LiquidacionesController.insertar(liquidacion)
        liquidacion_buscada = LiquidacionesController.buscar_por_id(id_insertado)
        self.assertTrue(liquidacion_buscada.esIgual(liquidacion))

if __name__ == '__main__':
    unittest.main()
