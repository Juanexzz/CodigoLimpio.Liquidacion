from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def Inicio():
    return render_template("inicio.html")

@app.route('/buscar')
def Buscar():
    return render_template("buscar.html")

@app.route('/insertar')
def Insertar():
    return render_template("insertar.html")

@app.route('/modificar')
def Modificar():
    return render_template("modificar.html")

@app.route('/')
def index():
    return render_template("inicio.html") # O la página que quieras como principal

if __name__ == '__main__':
    app.run(debug=True)