""" Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela. """


# Lista de dados
dado = dict()

# Entrada de dados

dado['Nome'] = str(input('Nome do aluno: '))
dado['Média'] = float(input('Média do aluno: '))

# Tratamento dos dados e Output
print('-=' * 30)
if dado['Média'] < 7:
    print(f'O aluno {dado["Nome"]} foi reprovado!')
else:
    print(f'O aluno {dado["Nome"]} foi aprovado!')
print('-=' * 30)



