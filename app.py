from flask import Flask, render_template, request
import sys
sys.path.append("src")
from view.web import plano


app = Flask(__name__, template_folder='src/view/web/templates')

app.register_blueprint(plano.blueprint)

if __name__ == '__main__':
    app.run(debug=True)
