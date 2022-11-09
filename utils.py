from models import Pessoas, Usuarios

# Insere dados tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Samuel', idade=25)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Gabriel').first()
    print(pessoa.idade)

# Altera dados na tabela Pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Oliveira').first()
    pessoa.nome = 'Irineu'
    pessoa.save()

# Exclui dados na Tabela Pessoa
def excluir_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Irineu').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('gabriel', '1234')
    insere_usuario('irineu', '4321')
    consulta_todos_usuarios()
    # insere_pessoas()
    # altera_pessoas()
    # consulta_pessoas()
    # excluir_pessoas()
