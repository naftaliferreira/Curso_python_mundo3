""" Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em um dicionário. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. """


# bibliotecas 

from random import randint
from time import sleep
from operator import itemgetter


# Dicionário e lista

game = {'Jogador-1': randint(1, 6),
        'Jogador-2': randint(1, 6), 
        'Jogador-3': randint(1, 6), 
        'Jogador-4': randint(1, 6)}

ranking = list()
# Valores sorteados

print('-=' * 50)
print('Valores sorteados:')
for k, v in game.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

# Ranking
# sorted para colocar o dicionário em ordem, a função itemgetter permite selecionar via indice qual será o valor critério para a ordem, reverse= serve para inverter a ordem
# Porem depois do tratamento abaixo ele irá transformar o dicionário em uma lista com tuplas dentro. 
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)  
print('-=' * 50)
print('     Ranking     ')

for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)


print('End Game')


