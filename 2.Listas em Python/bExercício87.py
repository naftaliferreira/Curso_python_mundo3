""" Aprimore o desafio anterior, mostrando no final:  

  A) A soma de todos os valores pares digitados.  

  B) A soma dos valores da terceira coluna. 

 C) O maior valor da segunda linha."""


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

sompar = somterc = somseg = 0

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