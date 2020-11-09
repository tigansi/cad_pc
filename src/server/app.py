from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS
from Computador import Computador

import json

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return ""


@app.route("/computador", methods=["POST"])
def computador():
    if(request.method == "POST"):
        data = json.loads(request.get_data())
        if(data["tipo"] == "cad_pc"):
            computador = Computador()
            return json.dumps(computador.cadastra_computador(data))


if __name__ == '__main__':
    app.run(
        debug=True,
        host="192.168.6.16")
    app.config['TEMPLATES_AUTORELOAD'] = True
