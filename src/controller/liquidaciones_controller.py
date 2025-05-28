import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  

import psycopg2
from src.model.empleado_liquidacion import EmpleadoLiquidacion
from src import SecretConfig

def ruta_sql(nombre_archivo):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../sql", nombre_archivo))


class LiquidacionesController:

    @staticmethod
    def crear_tabla():
        cursor = LiquidacionesController.obtener_cursor()

        with open(ruta_sql("crear-liquidaciones.sql"), "r") as archivo:

            consulta = archivo.read()

        cursor.execute(consulta)
        cursor.connection.commit()

    @staticmethod
    def borrar_tabla():
        cursor = LiquidacionesController.obtener_cursor()

        with open(ruta_sql("borrar-liquidaciones.sql"), "r") as archivo:

            consulta = archivo.read()

        cursor.execute(consulta)
        cursor.connection.commit()

    @staticmethod
    def insertar(liquidacion: EmpleadoLiquidacion) -> int:
        """Inserta una instancia de EmpleadoLiquidacion en la base de datos y retorna el ID"""
        cursor = LiquidacionesController.obtener_cursor()

        with open(ruta_sql("insertar-liquidacion.sql"), "r") as archivo:
            consulta = archivo.read()

        datos = (
            liquidacion.salario_auxilio,
            liquidacion.salario_sin_auxilio,
            liquidacion.salario_variable,
            liquidacion.fecha_inicio,
            liquidacion.fecha_fin,
            liquidacion.dias_suspension,
            liquidacion.dias_indemnizacion
        )

        cursor.execute(consulta, datos)
        id_insertado = cursor.fetchone()[0]
        cursor.connection.commit()
        return id_insertado


    @staticmethod
    def buscar_por_id(id_liquidacion) -> EmpleadoLiquidacion:
        """Devuelve una instancia de EmpleadoLiquidacion dado su ID"""
        cursor = LiquidacionesController.obtener_cursor()

        with open(ruta_sql("buscar-liquidacion-por-id.sql"), "r") as archivo:

            consulta = archivo.read()

        cursor.execute(consulta, (id_liquidacion,))
        fila = cursor.fetchone()
        if fila is None:
            return None

        return EmpleadoLiquidacion(
            salario_auxilio=fila[0],
            salario_sin_auxilio=fila[1],
            salario_variable=fila[2],
            fecha_inicio=fila[3].strftime("%d/%m/%Y"),
            fecha_fin=fila[4].strftime("%d/%m/%Y"),
            dias_suspension=fila[5],
            dias_indemnizacion=fila[6]
        )

    @staticmethod
    def borrar_por_id(id_liquidacion: int):
        """Elimina una fila por ID"""
        cursor = LiquidacionesController.obtener_cursor()

        with open(ruta_sql("borrar-liquidacion-por-id.sql"), "r") as archivo:

            consulta = archivo.read()

        cursor.execute(consulta, (id_liquidacion,))
        cursor.connection.commit()

    @staticmethod
    def modificar_por_id(id_liquidacion: int, nueva: EmpleadoLiquidacion):
        """Modifica una fila existente dado su ID"""
        cursor = LiquidacionesController.obtener_cursor()

        # Verificar si el ID existe
        cursor.execute("SELECT COUNT(*) FROM liquidacion_empleado WHERE id = %s", (id_liquidacion,))
        count = cursor.fetchone()[0]
        if count == 0:
            raise Exception(f"No existe un registro con el ID {id_liquidacion}")

        # Validaciones
        if nueva.salario_auxilio < 0 or nueva.salario_sin_auxilio < 0 or nueva.salario_variable < 0:
            raise Exception("Los valores salariales no pueden ser negativos.")

        # No es necesario validar si las fechas son None aquí, ya que en plano.py lo manejamos

        # Leer y ejecutar la consulta SQL desde archivo
        with open(ruta_sql("modificar-liquidacion-por-id.sql"), "r") as archivo:
            consulta = archivo.read()

        datos = (
            nueva.salario_auxilio,
            nueva.salario_sin_auxilio,
            nueva.salario_variable,
            nueva.fecha_inicio,
            nueva.fecha_fin,
            nueva.dias_suspension,
            nueva.dias_indemnizacion,
            id_liquidacion
        )

        cursor.execute(consulta, datos)
        cursor.connection.commit()

    @staticmethod
    def obtener_cursor():
        connection = psycopg2.connect(
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            host=SecretConfig.PGHOST,
        )
        return connection.cursor()