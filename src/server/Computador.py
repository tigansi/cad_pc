from psycopg2.extras import RealDictCursor
from Banco import Banco
import psycopg2
import json


class Computador:
    def __init__(self):
        pass

    def cadastra_computador(self, dados: list()) -> {}:
        try:
            banco = Banco()
            curso = banco.conectar()

            for i in dados:
                print(i)

            resul = {"msg": "teste", "sucesso": False}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()
        return resul
