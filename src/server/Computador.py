from psycopg2.extras import RealDictCursor
from Banco import Banco
import psycopg2
import json


class Computador:
    def __init__(self):
        pass

    def cadastra_computador(self, nr_patrimonio,
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
                            rel_tecnico):
        try:
            banco = Banco()
            curso = banco.conectar()

            print(nr_patrimonio)

            sql = """SELECT
                        nm_dominio
                    FROM computadores
                    WHERE ip_computador = %s"""

            val = (ip_computador, )
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
                                    tp_equipamento,
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

                val = (nr_patrimonio, ip_computador, tp_equipamento,
                       is_alugado, nm_dominio, user_ad, nm_user,
                       setor, office, prog_especial, tp_processador,
                       mem_ram, env_preventiva, rel_tecnico)

                curso.execute(sql, val)
                banco.commit()
                
                resul = {"msg": "Dados Cadastrados com sucesso",
                         "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul
