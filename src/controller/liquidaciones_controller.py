import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  

import psycopg2
from model.empleado_liquidacion import EmpleadoLiquidacion  
import SecretConfig


class LiquidacionesController:

    @staticmethod
    def crear_tabla():
        cursor = LiquidacionesController.obtener_cursor()

        with open("sql/crear-liquidaciones.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)
        cursor.connection.commit()

    @staticmethod
    def borrar_tabla():
        cursor = LiquidacionesController.obtener_cursor()

        with open("sql/borrar-liquidaciones.sql", "r") as archivo:
            consulta = archivo.read()

        cursor.execute(consulta)
        cursor.connection.commit()

    @staticmethod
    def insertar(liquidacion: EmpleadoLiquidacion) -> int:
        """Inserta una instancia de EmpleadoLiquidacion en la base de datos y retorna el ID"""
        cursor = LiquidacionesController.obtener_cursor()

        cursor.execute(f"""
            INSERT INTO liquidacion_empleado (
                salario_auxilio, salario_sin_auxilio, salario_variable,
                fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion
            ) VALUES (
                {liquidacion.salario_auxilio}, {liquidacion.salario_sin_auxilio}, {liquidacion.salario_variable},
                '{liquidacion.fecha_inicio.date()}', '{liquidacion.fecha_fin.date()}',
                {liquidacion.dias_suspension}, {liquidacion.dias_indemnizacion}
            ) RETURNING id
        """)

        id_insertado = cursor.fetchone()[0]
        cursor.connection.commit()
        return id_insertado

    @staticmethod
    def buscar_por_id(id_liquidacion) -> EmpleadoLiquidacion:
        """Devuelve una instancia de EmpleadoLiquidacion dado su ID"""
        cursor = LiquidacionesController.obtener_cursor()

        cursor.execute(f"""
            SELECT salario_auxilio, salario_sin_auxilio, salario_variable,
                   fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion
            FROM liquidacion_empleado WHERE id = {id_liquidacion}
        """)

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
        cursor.execute(f"DELETE FROM liquidacion_empleado WHERE id = {id_liquidacion}")
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

        # Validar que los valores sean válidos
        if nueva.salario_auxilio < 0 or nueva.salario_sin_auxilio < 0 or nueva.salario_variable < 0:
            raise Exception("Los valores salariales no pueden ser negativos.")

        if not nueva.fecha_inicio or not nueva.fecha_fin:
            raise Exception("Las fechas de inicio y fin no pueden ser vacías.")
        
        # Realizar la actualización
        cursor.execute(f"""
            UPDATE liquidacion_empleado SET
                salario_auxilio = %s,
                salario_sin_auxilio = %s,
                salario_variable = %s,
                fecha_inicio = %s,
                fecha_fin = %s,
                dias_suspension = %s,
                dias_indemnizacion = %s
            WHERE id = %s
        """, (
            nueva.salario_auxilio,
            nueva.salario_sin_auxilio,
            nueva.salario_variable,
            nueva.fecha_inicio.date(),
            nueva.fecha_fin.date(),
            nueva.dias_suspension,
            nueva.dias_indemnizacion,
            id_liquidacion
        ))

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
