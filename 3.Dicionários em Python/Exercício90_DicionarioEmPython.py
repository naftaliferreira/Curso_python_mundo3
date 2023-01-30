""" Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela. """


# Lista de dados
aluno = dict()

# Entrada de dados

aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'A média de {aluno["nome"]}: '))

# Tratamento dos dados e Output
print('-=' * 30)
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

# laço para cada chave e valor nos itens da lista. 
for k, v in aluno.items():
    print(f' - {k}: {v}')
print('-=' * 30)
print()



