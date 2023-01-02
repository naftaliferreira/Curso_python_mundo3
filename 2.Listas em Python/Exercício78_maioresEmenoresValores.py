"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista. """

# Adicionando itens a lista
lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

# Maiores e menores valores 
menor = min(lista)
maior = max(lista)

# Exibição de resultados
print(f'O menor valor inserido está na posção {lista.index(menor)} o número {menor}')
print(f'e o maior valor inserido está na posição {lista.index(maior)} é o número {maior}')

