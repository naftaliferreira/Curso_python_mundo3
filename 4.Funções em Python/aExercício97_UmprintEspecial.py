""" Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável

ex:
escreva('Olá mundo!')

saída: 
---------
olá mundo
---------
"""
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# programa principal
escreva('Hello world')
escreva('Curso em Vídeo Python')
escreva('Mundo 3')

