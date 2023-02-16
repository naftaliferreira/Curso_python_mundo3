
"""Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade()

Faça também um programa que importe esse módulo e use algumas dessas funções. 
 """


# Bibliotecas
import moeda

# Programa principal 

preco = float(input('Digite o preço: $ '))

print(f'O dobro de R${preco} é R$ {moeda.dobro(preco)}')
print(f'A metade de R${preco} é R$ {moeda.metade(preco)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preco, 10)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(preco, 10)} ')