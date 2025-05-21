
from flask import Flask

from flask import render_template, request
app = Flask(__name__)

@app.route('/buscar')
def Buscar():
    return render_template("buscar.html")
@app.route('/insertar')
def Insertar():
    return render_template("insertar.html")
@app.route('/modificar')
def Modificar():
    return render_template("modificar.html")

if __name__=='__main__':
   app.run( debug=True)
