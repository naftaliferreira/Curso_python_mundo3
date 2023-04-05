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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade='0'):
    try:
        a = open(arq, 'at')  # 'at' função interna append text
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()




