""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função vai
 mostrar a soma de todos os valores pares sorteados pela função anterior.  """

# bibliotecas
from random import randint
from time import sleep

# lista


 # funções 
def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f' {n}', end=' ', flush=True)
        sleep(0.3)
    print('fim')

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'somando os valores pares de {lista}, temos {soma}')

 # programas principais
numeros = list()

sorteia(numeros)

somaPar(numeros)
