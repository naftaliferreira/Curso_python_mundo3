""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e 
todos os dicionários em uma lista. 
No final, mostre: 

a) Quantas pessoas foram cadastradas?

b) A média de idade do grupo

c) Uma lista com todas as mulheres 

d) Uma lista com todas as pessoas com idade acima da média."""

# Armazenamento de dados

galera = list()
pessoa = dict()
tot = 0
# Input 
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    tot += 1
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resposta == 'N':
        break
# Tratamento de dados
print('-=' * 30)

# Quantas pessoas foram cadastradas?
print(f'Foram cadastradas {tot} pessoas.')

# A média de idade do grupo


# Uma lista com todas as mulheres 


# Uma lista com todas as pessoas com idade acima da média.

