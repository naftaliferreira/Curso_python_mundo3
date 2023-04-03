""" Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""


# Bibliotecas
from utilidadesCeV import moeda, dado  # Foi necessário retirar o ex111. do nome de módulo, o vscode não reconheceu por nada. 


# Programa principal 

preco = float(input('Digite o preço: R$ '))

moeda.resumo(preco, 15, 10)

