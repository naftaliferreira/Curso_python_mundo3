""" Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, 
se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
alem da idade, com quantos anos a pessoa vai se aposentar.  """

# bibliotecas
from time import sleep
from datetime import datetime

# Dicionário

dados_trabalhador = dict()

# dados auxiliares

aposent = 35  # aposenta com 35 anos de colaboração

# entrada de dados
print('-=' * 30)
dados_trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados_trabalhador['idade'] = datetime.now().year - nascimento
dados_trabalhador['ctps'] = int(input('Numero da carteira de trabalho: (0 caso não tenha) '))
if dados_trabalhador['ctps'] != 0:
    dados_trabalhador['ano contratação'] = int(input('Ano da contratação: '))
    dados_trabalhador['salário'] = float(input('Salário: '))
    dados_trabalhador['aposentadoria'] = dados_trabalhador['idade'] + ((dados_trabalhador['ano contratação'] + 35) - datetime.now().year)
    print('Cadastro concluído!')
else:
    print('Cadastro concluído!')
     
# Output
print('-=' * 30)

for k, v in dados_trabalhador.items():
    print(f' - {k}:  {v}')
