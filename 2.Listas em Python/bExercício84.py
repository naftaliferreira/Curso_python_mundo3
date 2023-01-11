""" Faça um programa que leia o nome e peso, de várias pessoas, 
guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas 

b) Uma listagem com as pessoas mais pesadas. 

c) Uma listagem com as pessoas mais leves """

# lista vazia
dados_grupo = list()
dados_indiv = list()

# contagem de usuários cadastrados
tot = 0

# entrada de dados em loop
while True:
    dados_indiv.append(str(input('Digite o nome: ')))
    dados_indiv.append(int(input('Digite a idade: ')))
    
# Copiando os dados da lista individual para a lista grupo
    dados_grupo.append(dados_indiv[:])
    dados_indiv.clear()
    tot += 1
   
    

# Condição para continuar
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
            break    

# Total de pessoas cadastradas
print(f'Foram cadastradas um total de {tot} pessoas.')

# maior peso


# menor peso



