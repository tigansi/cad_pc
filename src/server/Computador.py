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

            sql = """SELECT
                        nm_dominio
                    FROM computadores
                    WHERE ip_computador = %s"""

            val = (dados["ip_computador"], )
            curso.execute(sql, val)
            dados = curso.fetchall()

            if(len(dados) > 0):
                resul = {"msg": "O computador já foi cadastrado",
                         "sucesso": False}
            else:
                sql = """INSERT
                            INTO
                        computadores(nr_patrimonio,
                                    ip_computador,
                                    tp_equipamento
                                    is_alugado,
                                    nm_dominio,
                                    user_ad,
                                    nm_user,
                                    setor,
                                    office,
                                    prog_especial,
                                    tp_processador,
                                    mem_ram,
                                    env_preventiva,
                                    rel_tecnico)
                        VALUES(%s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s)"""

                val = (dados["nr_patrimonio"], dados["ip_computador"],
                       dados["tp_equipamento"], dados["is_alugado"],
                       dados["nm_dominio"], dados["user_ad"],
                       dados["nm_user"], dados["setor"], dados["office"],
                       dados["prog_especial"], dados["tp_processador"],
                       dados["mem_ram"], dados["env_preventiva"],
                       dados["rel_tecnico"])

                curso.execute(sql, val)
                banco.commit()

                resul = {"msg": "Dados Cadastrados com sucesso",
                         "sucesso": False}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()
        return resul
