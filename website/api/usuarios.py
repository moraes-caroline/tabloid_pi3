from unicodedata import category
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for, abort
from flask_login import login_required, current_user



from ..mysql import mydb

api = Blueprint('usuarios', __name__)

#---------------------------USUARIOS GET-------------------------------------------------------
@api.route('/api/usuarios', methods=['GET'])
def getUsuario():
    try:
        cursor = mydb.cursor()
        sql = "SELECT * FROM usuario"
        cursor.execute(sql)

        users = cursor.fetchall()
        userList = list()
        for usuario in users:
            userList.append(
                {
                'id': usuario[0],
                'nome': usuario[1],
                'cpf': usuario[2],
                'email': usuario[3],
                'telefone': usuario[4]


                }
            )
        return jsonify(
            mensagem = 'Lista de Usuários',
            dados= userList
        )
    except Exception as ex:
        return jsonify({'menssagem': "ERRO: dados não existe!"})


#---------------------------USUARIOS ID--------------------------------------------------------
@api.route('/api/usuarios/<int:id>', methods=['GET'])
def obter_usuario_por_id(id):
    try:
        cursor = mydb.cursor()

        sql = "SELECT * FROM usuario WHERE id = '{0}' ".format(id)
        cursor.execute(sql)
    
        user = cursor.fetchone()
        
        dados = {'id':user[0], 'nome':user[1],'cpf':user[2], 'email':user[3], 'telefone':user[4] }
        return jsonify(dados)
    except Exception as ex:
        return jsonify ({'menssagem': "Erro: registro não encontrado!"})

#-------------------------POST------------------------------------------------
@api.route('/api/usuarios', methods=['POST'])
def incluir_usuario():
    try:
        user = request.json
        cursor = mydb.cursor()
        sql ="""INSERT INTO usuario (id,nome,cpf, email, telefone) VALUES({0},'{1}','{2}','{3}','{4}')""".format(user['id'],user['nome'], user['cpf'], user['email'], user['telefone'])
        cursor.execute(sql)
        mydb.commit()

        return jsonify(
            mensagem="Usuário cadastrado com sucesso",
        )
    except Exception as ex:
        return jsonify({'menssagem': "Error"})
#-----------------------------------------------------------------------------------


#----------------------DELETE------------------------------------------------------
@api.route('/api/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    try:
        cursor = mydb.cursor()

        sql = "DELETE FROM usuario WHERE id = '{0}' ".format(id)
        cursor.execute(sql)
    
        mydb.commit()
        
        return jsonify({'menssagem': "Registro deletado com sucesso!"})
    except Exception as ex:
        return jsonify ({'menssagem': "Erro: registro não encontrado!"})

#------------------------UPATE-----------------------------------------------------
@api.route('/api/usuarios/<id>', methods=['PUT'])
def atualizar_usuario(id):
    try:
        user = request.json
        cursor = mydb.cursor()

        sql = """UPDATE  usuario SET nome='{0}', cpf='{1}', email='{2}', telefone='{3}' WHERE id = {4} """.format(user['nome'], user['cpf'], user['email'], user['telefone'], id)
        cursor.execute(sql)
    
        mydb.commit()
        
        return jsonify({'menssagem': "Registro atualizado com sucesso!"})
    except Exception as ex:
        return jsonify ({'menssagem': "Erro: atualização não realizada!"})
#-----------------------------------------------------------------------------------


