from flask import Blueprint, render_template, request
import sys
sys.path.append("src")
from src.controller.liquidaciones_controller import LiquidacionesController

blueprint = Blueprint("vista_usuarios", __name__, "templates")

@blueprint.route('/inicio')
def Inicio():
    return render_template("initio.html")

@blueprint.route('/buscar', methods=['GET', 'POST'])
def Buscar():
    if request.method == 'POST':
        id_busqueda = request.form['id_registro']
        liquidacion = LiquidacionesController.buscar_por_id(id_busqueda)
        return render_template("resultados_buscar.html", resultado=liquidacion)
    return render_template("buscar.html")

@blueprint.route('/insertar')
def Insertar():
    return render_template("insertar.html")

@blueprint.route('/modificar')
def Modificar():
    return render_template("modificar.html")

@blueprint.route('/')
def index():
    return render_template("initio.html")

@blueprint.errorhandler(Exception)
def manejar_error(err):
    return "Ocurrio un error" + str(err)