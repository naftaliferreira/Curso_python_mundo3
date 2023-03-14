""" Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma
 validação de dados para aceitar apenas valores que seja monetários."""


# Bibliotecas
from utilidadesCeV import moeda
from utilidadesCeV import dado  # Foi necessário retirar o ex111. do nome de módulo, o vscode não reconheceu por nada. 


# Programa principal 

preco = dado.leiadinheiro('Digite o preço: R$ ')

moeda.resumo(preco, 15, 10)
