""" Crie um programa que declare uma matriz de dimensão 3 X 3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):  # Laço para linha
    for c in range(0, 3): # Laço para coluna
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))

print('-*-' * 30)
for l in range(0 ,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    
