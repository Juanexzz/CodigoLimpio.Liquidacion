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

    # ---------------------------
    # INSERTAR
    # ---------------------------
    def test_insert_valido_1(self):
        liquidacion = EmpleadoLiquidacion(1500000, 1300000, 500000, "01/01/2023", "31/12/2023", 0, 15)
        id_insertado = LiquidacionesController.insertar(liquidacion)
        buscada = LiquidacionesController.buscar_por_id(id_insertado)
        self.assertTrue(buscada.esIgual(liquidacion))

    def test_insert_valido_2(self):
        liquidacion = EmpleadoLiquidacion(1200000, 1100000, 400000, "01/06/2023", "30/06/2023", 0, 5)
        id_insertado = LiquidacionesController.insertar(liquidacion)
        buscada = LiquidacionesController.buscar_por_id(id_insertado)
        self.assertTrue(buscada.esIgual(liquidacion))

    def test_insert_error_datos_faltantes(self):
        with self.assertRaises(Exception):
            # Falta salario_auxilio
            liquidacion = EmpleadoLiquidacion(None, 1100000, 400000, "01/06/2023", "30/06/2023", 0, 5)
            LiquidacionesController.insertar(liquidacion)

    # ---------------------------
    # MODIFICAR
    # ---------------------------
    def test_update_valido(self):
        liquidacion = EmpleadoLiquidacion(1000000, 950000, 200000, "01/01/2022", "31/01/2022", 2, 0)
        id_insertado = LiquidacionesController.insertar(liquidacion)

        # Modificar
        liquidacion.salario_auxilio = 1050000
        LiquidacionesController.modificar_por_id(id_insertado, liquidacion)

        buscada = LiquidacionesController.buscar_por_id(id_insertado)
        self.assertEqual(buscada.salario_auxilio, 1050000)

    def test_update_valores_invalidos(self):
        liquidacion = EmpleadoLiquidacion(1000000, 950000, 200000, "01/01/2022", "31/01/2022", 2, 0)
        id_insertado = LiquidacionesController.insertar(liquidacion)

        # Intentar modificar con datos inválidos
        liquidacion.salario_auxilio = -50000  # Valor inválido
        with self.assertRaises(Exception):
            LiquidacionesController.modificar_por_id(id_insertado, liquidacion)

    def test_update_id_inexistente(self):
        liquidacion = EmpleadoLiquidacion(1000000, 950000, 200000, "01/01/2022", "31/01/2022", 2, 0)
        with self.assertRaises(Exception):
            LiquidacionesController.modificar_por_id(9999, liquidacion)

    # ---------------------------
    # BUSCAR
    # ---------------------------
    def test_buscar_valido(self):
        liquidacion = EmpleadoLiquidacion(1400000, 1200000, 300000, "01/05/2022", "31/05/2022", 0, 0)
        id_insertado = LiquidacionesController.insertar(liquidacion)
        buscada = LiquidacionesController.buscar_por_id(id_insertado)
        self.assertTrue(buscada.esIgual(liquidacion))

    def test_buscar_id_inexistente(self):
        resultado = LiquidacionesController.buscar_por_id(99999)
        self.assertIsNone(resultado)

    def test_buscar_id_invalido(self):
        with self.assertRaises(Exception):
            LiquidacionesController.buscar_por_id("invalido")

if __name__ == '__main__':
    unittest.main()
