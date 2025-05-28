from flask import Blueprint, render_template, request, redirect, url_for
import sys
sys.path.append("src")
from controller.liquidaciones_controller import LiquidacionesController
from datetime import datetime
from model.empleado_liquidacion import EmpleadoLiquidacion

blueprint = Blueprint("vista_usuarios", __name__, "templates")

@blueprint.route('/inicio')
def Inicio():
    return render_template("initio.html")

@blueprint.route('/buscar', methods=['GET', 'POST'])
def Buscar():
    if request.method == 'POST':
        id_busqueda = request.form.get('id_registro')
        if not id_busqueda:
            return render_template("error.html", error="El ID del registro es obligatorio para buscar."), 400
        liquidacion = LiquidacionesController.buscar_por_id(id_busqueda)
        if not liquidacion:
            return render_template("error.html", error=f"No se encontró liquidación con ID {id_busqueda}."), 404
        return render_template("resultados_buscar.html", resultado=liquidacion)
    return render_template("buscar.html")

@blueprint.route('/insertar', methods=['GET', 'POST'])
def Insertar():
    if request.method == 'POST':
        sueldo_str = request.form.get('sueldo')
        sueldo_auxilio_str = request.form.get('sueldo_auxilio')
        fecha_ingreso_str = request.form.get('fecha_ingreso')
        fecha_retiro_str = request.form.get('fecha_retiro')
        salario_variable_str = request.form.get('salario_variable')
        dias_suspension_str = request.form.get('dias_suspension')
        dias_indemnizacion_str = request.form.get('dias_indemnizacion')

        if not sueldo_str:
            return render_template("error.html", error="El sueldo es obligatorio."), 400
        if not sueldo_auxilio_str:
            return render_template("error.html", error="El sueldo con auxilio es obligatorio."), 400
        if not fecha_ingreso_str:
            return render_template("error.html", error="La fecha de ingreso es obligatoria."), 400
        if not fecha_retiro_str:
            return render_template("error.html", error="La fecha de retiro es obligatoria."), 400
        if not salario_variable_str:
            return render_template("error.html", error="El salario variable es obligatorio."), 400
        if not dias_suspension_str:
            return render_template("error.html", error="Los días de suspensión son obligatorios."), 400
        if not dias_indemnizacion_str:
            return render_template("error.html", error="Los días de indemnización son obligatorios."), 400

        try:
            sueldo = float(sueldo_str)
            sueldo_auxilio = float(sueldo_auxilio_str)
            salario_variable = float(salario_variable_str)
            dias_suspension = int(dias_suspension_str)
            dias_indemnizacion = int(dias_indemnizacion_str)
        except ValueError:
            return render_template("error.html", error="Por favor, ingresa valores numéricos válidos."), 400

        fecha_inicio_procesada = None
        try:
            fecha_inicio_procesada = datetime.strptime(fecha_ingreso_str, '%Y-%m-%d').date()
        except ValueError:
            try:
                fecha_inicio_procesada = datetime.strptime(fecha_ingreso_str, '%m/%d/%Y').date()
            except ValueError as e:
                print(f"Error al convertir fecha de ingreso: {e}, valor recibido: '{fecha_ingreso_str}'")
                return render_template("error.html", error="Formato de fecha de ingreso incorrecto. Debe ser AAAA-MM-DD o MM/DD/AAAA."), 400

        fecha_fin_procesada = None
        try:
            fecha_fin_procesada = datetime.strptime(fecha_retiro_str, '%Y-%m-%d').date()
        except ValueError:
            try:
                fecha_fin_procesada = datetime.strptime(fecha_retiro_str, '%m/%d/%Y').date()
            except ValueError as e:
                print(f"Error al convertir fecha de retiro: {e}, valor recibido: '{fecha_retiro_str}'")
                return render_template("error.html", error="Formato de fecha de retiro incorrecto. Debe ser AAAA-MM-DD o MM/DD/AAAA."), 400

        nueva_liquidacion = EmpleadoLiquidacion(
            salario_auxilio=sueldo_auxilio,
            salario_sin_auxilio=sueldo,
            salario_variable=salario_variable,
            fecha_inicio=fecha_inicio_procesada,
            fecha_fin=fecha_fin_procesada,
            dias_suspension=dias_suspension,
            dias_indemnizacion=dias_indemnizacion
        )

        try:
            id_insertado = LiquidacionesController.insertar(nueva_liquidacion)
            return render_template("insercion_exitosa.html", id_insertado=id_insertado)
        except Exception as e:
            return render_template("error.html", error=str(e)), 500
    return render_template("insertar.html")

@blueprint.route('/modificar', methods=['GET', 'POST'])
def Modificar():
    if request.method == 'POST':
        id_modificar_str = request.form.get('id_modificar')
        if not id_modificar_str:
            return render_template("error.html", error="El ID del registro a modificar es obligatorio."), 400

        try:
            id_modificar = int(id_modificar_str)
        except ValueError:
            return render_template("error.html", error="El ID debe ser un número entero."), 400

        sueldo_str = request.form.get('sueldo')
        sueldo_auxilio_str = request.form.get('sueldo_auxilio')
        fecha_ingreso_str = request.form.get('fecha_ingreso')
        fecha_retiro_str = request.form.get('fecha_retiro')
        salario_variable_str = request.form.get('salario_variable')
        dias_suspension_str = request.form.get('dias_suspension')
        dias_indemnizacion_str = request.form.get('dias_indemnizacion')

        liquidacion_actual = LiquidacionesController.buscar_por_id(id_modificar)
        if not liquidacion_actual:
            return render_template("error.html", error=f"No se encontró liquidación con ID {id_modificar}"), 404

        sueldo = float(sueldo_str) if sueldo_str else liquidacion_actual.salario_sin_auxilio
        sueldo_auxilio = float(sueldo_auxilio_str) if sueldo_auxilio_str else liquidacion_actual.salario_auxilio
        salario_variable = float(salario_variable_str) if salario_variable_str else liquidacion_actual.salario_variable
        dias_suspension = int(dias_suspension_str) if dias_suspension_str else liquidacion_actual.dias_suspension
        dias_indemnizacion = int(dias_indemnizacion_str) if dias_indemnizacion_str else liquidacion_actual.dias_indemnizacion

        fecha_inicio_procesada = None
        if fecha_ingreso_str:
            try:
                fecha_inicio_procesada = datetime.strptime(fecha_ingreso_str, '%Y-%m-%d').date()
            except ValueError:
                try:
                    fecha_inicio_procesada = datetime.strptime(fecha_ingreso_str, '%m/%d/%Y').date()
                except ValueError as e:
                    print(f"Error al convertir fecha de ingreso (modificar): {e}, valor recibido: '{fecha_ingreso_str}'")
                    return render_template("error.html", error="Formato de fecha de ingreso incorrecto."), 400
        else:
            fecha_inicio_procesada = liquidacion_actual.fecha_inicio

        fecha_fin_procesada = None
        if fecha_retiro_str:
            try:
                fecha_fin_procesada = datetime.strptime(fecha_retiro_str, '%Y-%m-%d').date()
            except ValueError:
                try:
                    fecha_fin_procesada = datetime.strptime(fecha_retiro_str, '%m/%d/%Y').date()
                except ValueError as e:
                    print(f"Error al convertir fecha de retiro (modificar): {e}, valor recibido: '{fecha_retiro_str}'")
                    return render_template("error.html", error="Formato de fecha de retiro incorrecto."), 400
        else:
            fecha_fin_procesada = liquidacion_actual.fecha_fin

        nueva_liquidacion = EmpleadoLiquidacion(
            salario_auxilio=sueldo_auxilio,
            salario_sin_auxilio=sueldo,
            salario_variable=salario_variable,
            fecha_inicio=fecha_inicio_procesada,
            fecha_fin=fecha_fin_procesada,
            dias_suspension=dias_suspension,
            dias_indemnizacion=dias_indemnizacion
        )

        try:
            LiquidacionesController.modificar_por_id(id_modificar, nueva_liquidacion)
            return render_template("modificacion_exitosa.html", id_modificado=id_modificar)
        except Exception as e:
            return render_template("error.html", error=str(e)), 500

    return render_template("modificar.html")

@blueprint.route('/crear_tabla')
def CrearTabla():
    try:
        LiquidacionesController.crear_tabla()
        return render_template("initio.html", mensaje="La tabla de liquidaciones fue creada exitosamente.")
    except Exception as e:
        return render_template("error.html", error=f"Error al crear la tabla: {str(e)}"), 500

@blueprint.route('/borrar_tabla')
def BorrarTabla():
    try:
        LiquidacionesController.borrar_tabla()
        return render_template("initio.html", mensaje="La tabla de liquidaciones fue eliminada exitosamente.")
    except Exception as e:
        return render_template("error.html", error=f"Error al borrar la tabla: {str(e)}"), 500


@blueprint.route('/')
def index():
    return render_template("initio.html")

@blueprint.errorhandler(Exception)
def manejar_error(err):
    return render_template("error.html", error=str(err)), 500
