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

            nr_patrimonio = str(data["nr_patrimonio"])
            ip_computador = str(data["ip_equipamento"])
            tp_equipamento = str(data["tp_equipamento"])
            is_alugado = str(data["is_alugado"])
            nm_dominio = str(data["nm_dominio"])
            user_ad = str(data["ad_user"])
            nm_user = str(data["nm_user"])
            setor = str(data["setor"])
            office = str(data["office"])
            prog_especial = data["prog_especial"]
            tp_processador = data["tp_processador"]
            mem_ram = data["mem_ram"]
            env_preventiva = data["env_preventiva"]
            rel_tecnico = data["rel_tecnico"]

            return json.dumps(computador.cadastra_computador(nr_patrimonio,
                                                             ip_computador,
                                                             tp_equipamento,
                                                             is_alugado,
                                                             nm_dominio,
                                                             user_ad,
                                                             nm_user, setor,
                                                             office,
                                                             prog_especial,
                                                             tp_processador,
                                                             mem_ram,
                                                             env_preventiva,
                                                             rel_tecnico))

        elif(data["tipo"] == "list_pc_filtro"):
            computador = Computador()
            return ""


if __name__ == '__main__':
    app.run(
        debug=True,
        host="192.168.6.16")
    app.config['TEMPLATES_AUTORELOAD'] = True
