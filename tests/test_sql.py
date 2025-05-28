import unittest
import sys
sys.path.append("src")

from src.model.empleado_liquidacion import EmpleadoLiquidacion
from src.controller.liquidaciones_controller import LiquidacionesController

class TestLiquidacionEmpleado(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        LiquidacionesController.borrar_tabla()
        LiquidacionesController.crear_tabla()

    def test_insert_error_datos_faltantes(self):
        with self.assertRaises(Exception):
            # Falta salario_auxilio
            liquidacion = EmpleadoLiquidacion(None, 1100000, 400000, "01/06/2023", "30/06/2023", 0, 5)
            LiquidacionesController.insertar(liquidacion)


    def test_update_id_inexistente(self):
        liquidacion = EmpleadoLiquidacion(1000000, 950000, 200000, "01/01/2022", "31/01/2022", 2, 0)
        with self.assertRaises(Exception):
            LiquidacionesController.modificar_por_id(9999, liquidacion)

    # ---------------------------
    # BUSCAR
    # ---------------------------


    def test_buscar_id_inexistente(self):
        resultado = LiquidacionesController.buscar_por_id(99999)
        self.assertIsNone(resultado)

    def test_buscar_id_invalido(self):
        with self.assertRaises(Exception):
            LiquidacionesController.buscar_por_id("invalido")

if __name__ == '__main__':
    unittest.main()
