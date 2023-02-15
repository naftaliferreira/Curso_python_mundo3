
"""Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade()

Faça também um programa que importe esse módulo e use algumas dessas funções. 
 """


# Bibliotecas
import moeda

# Programa principal 

Valor = float(input('Digite o preço: $ '))

print(f'O dobro de {Valor} é R$ {moeda.dobro(Valor)}')
print(f'A metade de {Valor} é R$ {moeda.metade(Valor)}')
print(f'Aumentando 10% é {moeda.aumento(Valor)}')
print(f'Diminuindo 10% é {moeda.diminuindo(Valor)}')