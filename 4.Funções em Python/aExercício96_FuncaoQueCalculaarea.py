""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno. """

def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno de {larg} x {comp} é {a}m²')



# Programa principal 
print('-' * 30)
print('   CONTROLE DE TERRENOS   ')
print('-' * 30)
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
area(l, c)