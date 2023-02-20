""" Exercício Python 108: 
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números
 como um valor monetário formatado."""

# Bibliotecas
import moeda

# Programa principal 

preco = float(input('Digite o preço: R$ '))

print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(preco, 10))}')

