"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: Início, Fim e Passo e realize a contagem. 

Seu programa tem que realizar três contagens através da função criada: 

a) De 1 até 10, de 1 em 1

b) De 10 a 0, de 2 em 2

c) Uma contagem personalizada.

"""
from time import sleep

def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} em {p}')
    sleep(2)
    # bloco para corrigir erro, quando for colocado passo negativo, desta forma o programa irá funcionar corretamente.
    if p < 0:
        p *= -1
    if p == 0: # corrigindo erro se usuário colocar 0 no passo, pois 0 não anda. 
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f' {cont}', end=' ', flush=True) # Devido as últimas atualizações do python a função sleep está gerando um buffer
            sleep(0.5)                             # de tela ao invés de intervalo para resolver isto, basta usar a função flush=True. 
            cont -= p
        print('FIM')


# Programa principal
contador(1, 10, 1)

contador(10, 0, 2)
print('-=' * 20)
print(' Agora é a sua vez ')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
salt = int(input('Salto: '))

contador(ini, fim, salt)