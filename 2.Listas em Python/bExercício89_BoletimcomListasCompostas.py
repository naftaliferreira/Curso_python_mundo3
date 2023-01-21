""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

turma = list()
aluno = list()

while True:
    nome = str(input('Nome do aluno: '))
    aluno.append(nome)
    nota1 = float(input('Insira a primeira nota: '))
    aluno.append(nota1)
    nota2 = float(input('Digite a segunda nota: '))
    aluno.append(nota2)
    media = (nota1 + nota2) / 2
    aluno.append(media)
    turma.append(aluno[:])
    aluno.clear()
    resposta = str(input('Quer adicionar outro aluno? [S/N] '))
    if resposta in 'Nn':
        break



print('₪' * 50)
print('₪' * 11, 'Relatório de notas da turma', '₪' * 11)
print('₪' * 50)




