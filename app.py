from flask import Flask, render_template, request
import sys
sys.path.append("src")
from src.view.web import plano


app = Flask(__name__)

app.register_blueprint(plano.blueprint)

if __name__ == '__main__':
    app.run(debug=True)
