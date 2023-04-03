from lib.interface import *
from time import sleep

cabecalho('Sistema de Arquivos v1.0')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema')
        for i in range(0, 3):
            print('*')
            sleep(0.5)
        cabecalho('Até Logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)

