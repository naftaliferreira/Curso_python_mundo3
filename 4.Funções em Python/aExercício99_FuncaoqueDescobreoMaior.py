""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmentros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual é o maior. 
"""
from time import sleep

def maior(* num):
    cont = maior = 0
    print('Analisando os números ...')
    for v in num:
        print(f'{v}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior == 0
        if cont > 0:
            maior == num
    print(f'O maior número é {num}')



# Programa principal

maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()
 

