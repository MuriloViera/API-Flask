from flask import Flask, Blueprint, request, jsonify
import sqlite3

#Especificação de rota
garagem = Blueprint('garagem', __name__)

def conectar():
    return sqlite3.connect('database/data.db')

@garagem.route('/recurso2/', methods=['GET'])#Endpoint primario, o que vem dps do URL
def get_all():
    garagens = []
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_cliente")

        for i in cur.fetchall():
            garagem = {}
            garagem["id"] = i["id"]
            garagem["nome"] = i["nome"]
            garagem["marca"] = i["marca"]
            garagem["ano"] = i["ano"]
            garagens.append(garagem)
    except Exception as e:
        print(e)
        clientes = []

    return jsonify(garagens)

@garagem.route('recurso1/<id>', methods=['GET'])
def get_by_id(id):
    garagem = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_cliente where id=?",(id,))
        row = cur.fetchone()
       
        garagem["id"] = row["id"]
        garagem["nome"] = row["nome"]
        garagem["marca"] = row["marca"]
        garagem["ano"] = row["ano"]
           
    except Exception as e:
        print(str(e))
        garagem = {}

    return jsonify(garagem)    


@garagem.route('recurso1/',  methods = ['POST'])
def add():
    garagem = request.get_json()
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO tb_cliente (nome, marca, ano) VALUES (?, ?, ?)",
                    (garagem['nome'], garagem['marca'], garagem['ano']) )
        conn.commit()
        resposta = jsonify(
            {
                'mensagem':'Operacao realizada com sucesso',
                'id' : cur.lastrowid
            }
        )
    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()
    return resposta

@garagem.route('recurso4/',  methods = ['POST'])
def add_fusca():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO tb_cliente (nome, marca, ano) VALUES ('Fusca', 'Volkswagen', '1965')",
                    )
        conn.commit()
        resposta = jsonify(
            {
                'mensagem':'Operacao realizada com sucesso',
                'id' : cur.lastrowid
            }
        )
    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()
    return resposta    

@garagem.route('recurso3/',  methods = ['PUT'])
def update():
    garagem = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE tb_cliente SET nome=?, marca=?, ano=? WHERE id=?",
                    (garagem['nome'], garagem['marca'], garagem['ano'], garagem['id']) )
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta

@garagem.route('recurso5/',  methods = ['DELETE'])
def delete_fusca():

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM tb_cliente WHERE nome=?",("Fusca",))
        conn.commit()
        resposta = jsonify({'mensagem':'Registro apagado com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta

@garagem.route('recurso3/<id>',  methods = ['DELETE'])
def delete(id):
    print(id)
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM tb_cliente WHERE id=?",(id,))
        conn.commit()
        resposta = jsonify({'mensagem':'Registro apagado com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta