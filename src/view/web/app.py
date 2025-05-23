from flask import Flask, render_template, request
from src.controller.liquidaciones_controller import LiquidacionesController  # Importa el controlador

app = Flask(__name__)

@app.route('/inicio')
def Inicio():
    return render_template("inicio.html")

@app.route('/buscar', methods=['GET', 'POST'])
def Buscar():
    if request.method == 'POST':
        id_busqueda = request.form['id_registro']
        liquidacion = LiquidacionesController.buscar_por_id(id_busqueda)
        return render_template("resultados_buscar.html", resultado=liquidacion)
    return render_template("buscar.html")

@app.route('/insertar')
def Insertar():
    return render_template("insertar.html")

@app.route('/modificar')
def Modificar():
    return render_template("modificar.html")

@app.route('/')
def index():
    return render_template("inicio.html")

if __name__ == '__main__':
    app.run(debug=True)