""" Faça um programa que leia o nome e peso, de várias pessoas, 
guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas 

b) Uma listagem com as pessoas mais pesadas. 

c) Uma listagem com as pessoas mais leves """

# lista vazia
dados_temp = []
dados_princ = []
maior = menor = 0


# entrada de dados em loop
while True: 
    dados_temp.append(str(input('Digite aqui o seu nome: ')))
    dados_temp.append(int(input('Digite aqui o seu peso: ')))
    if len(dados_princ) == 0:
        maior = menor = dados_temp[1]
    else:
        if dados_temp[1] > maior:
            maior = dados_temp[1]
        if dados_temp[1] < menor:
            menor = dados_temp[1]
    
    dados_princ.append(dados_temp[:])
    dados_temp.clear()
# Condição para continuar
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break


print(f'As pessoas cadastradas foram {dados_princ}')
print(f'Ao todo foram cadastradas {len(dados_princ)} pessoas')

print(f'O maior peso foi de {maior}kg', end='')
for p in dados_princ:
    if p[1] == maior:
        print(f' O usuário com maior peso é [{p[0]}]')
print()

print(f'O menor peso foi de {menor}', end='')
for o in dados_princ:
    if p[1] == menor:
        print(f'O usuário com menor peso é [{p[0]}]')
print()
