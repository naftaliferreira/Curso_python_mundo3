""" Aprimore o desafio anterior, mostrando no final:  

  A) A soma de todos os valores pares digitados.  

  B) A soma dos valores da terceira coluna. 

 C) O maior valor da segunda linha."""


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

sompar = somterc = maior = 0

for l in range(0, 3):  # Laço para linha
    for c in range(0, 3): # Laço para coluna
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))

print('-*-' * 30)
for l in range(0 ,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sompar += matriz[l][c]
    print()
print('-=-' * 30)
print(f'A soma dos valores pares é {sompar}')
# Laço for apenas para a linha, pois o elemento da terceira coluna será fixado para somar. 
for l in range(0, 3):
    somterc += matriz[l][2]
# A soma dos valores da terceira linha
print(f'A soma dos números da terceira coluna é {somterc}.')

# O maior valor da segunda linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]


print(f'O maior valor da segunda linha são: {maior}.')