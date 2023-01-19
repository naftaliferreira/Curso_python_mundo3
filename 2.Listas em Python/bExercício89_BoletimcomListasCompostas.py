""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

dados_ind = list()
dados_turma = list()

while True:
    nome = str(input('Digite o nome do aluno: '))
    dados_ind.append(nome)
    pnota = float(input('Digite a primeira nota: '))
    dados_ind.append(pnota)
    snota = float(input('Digite a segunda nota: '))
    dados_ind.append(snota)

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        dados_turma.append(dados_ind[:])
        dados_ind.clear()
        break
    if resp in 'Ss':
        dados_turma.append(dados_ind[:])
        dados_ind.clear()

print(f'Os dados inseridos são: {dados_turma}')
