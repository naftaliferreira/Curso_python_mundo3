""" Faça um programa que ajude um jogador da MEGA-SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta"""

# Bibliotecas
from random import randint
from time import sleep

# Listas

dezenas = [[], [], [], [], [], []]
jogos = []

# Contadores

jogos = 0

# Menu Programa
print('Simulador de MEGA-SENA')
print()
print(''' Bem vindo!''')
print()
# programa
while True:

    n = int(input('Quantidade de jogos a serem gerados: '))

    for i in range(0, n):
        for i in range(0, 6):
            dezenas.append(randint(1, 60))
           
            jogos.append(dezenas[:])
            dezenas.clear()
            jogos += 1


    if n == jogos:
        for c, i in range(0, n):
            print(f'{c}º Sorteio: {i}')
            sleep(2)

    resp = str(input('Quer gerar novos números? [S/N] '))

    if resp in 'Nn':
        break

    print('Fim do programa!')

print('Volte sempre!')