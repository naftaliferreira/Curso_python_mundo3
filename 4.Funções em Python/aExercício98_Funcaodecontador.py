"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: Início, Fim e Passo e realize a contagem. 

Seu programa tem que realizar três contagens através da função criada: 

a) De 1 até 10, de 1 em 1

b) De 10 a 0, de 2 em 2

c) Uma contagem personalizada.

"""
# Função Contador comum 
def contador(i, f, p):
    print(f'Contagem de {i} até {f} em {p}')

    cont = i
    while cont <= f:
        print(f'{cont}', end=' ')
        cont += p
    print('Fim')

contador(1, 10, 1)



