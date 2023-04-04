from lib.interface import *

def arquivoExiste(name):
    try:
        a = open(name, 'rt') # rt = read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True 


def criaArquivo(nome):
    try:
        a = open(nome, 'wt+') # write text, +1 (caso não tenha o aquivo, o sistema cria)
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
 
        

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro na leitura do arquivo!')
    else:
        cabecalho('Pessoas Cadastradas')
        print(a.read())
