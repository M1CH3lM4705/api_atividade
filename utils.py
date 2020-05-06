from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Matos', idade=33)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Matos').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Matos').first()
    pessoa.idade = 32
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Matos')
    pessoa.delete()

if __name__=='__main__':
    #insere_pessoas()
    #altera_pessoa()
    consulta_pessoas()