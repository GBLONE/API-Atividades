from flask import Flask, request, json
from flask_restful import Resource, Api
from models import Pessoas, Atividades
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth
app = Flask(__name__)
api = Api(app)

USUARIOS = {
    'gabriel': '123',
    'samuel': '321'
}

@auth.verify_password()
def verificacao(login, senha):
    if not (login, senha):
        return False
    return USUARIOS.get(login) == senha


class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'Error',
                'mensagem': 'Pessoa não encontrada.'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensg = f'Pessoa {pessoa.nome} excluída com sucesso'
        pessoa.delete()
        return {'status': 'Sucesso',
                'mensagem': mensg}


class Lista_Pessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id,
                     'nome': i.nome,
                     'idade': i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class Lista_Atividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id,
                     'nome': i.nome,
                     'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(Lista_Pessoas, '/pessoa/') #listas Pessoas
api.add_resource(Lista_Atividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
