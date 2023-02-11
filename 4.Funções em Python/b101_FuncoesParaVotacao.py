"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições. """

# Bibliotecas
from datetime import datetime



# função
def voto(ano):
    """ 
    Função que verifica se o usuário pode ou não votar. 

        - Se o usuário tiver mais de 15 anos e menos de 18 anos ou tem mais de 65 anos, o seu voto é opcional. 
        - Se o usuário tiver entre 18 e 65 anos, o voto é obrigatório. 
        - Se o usuário tiver menos de 16 anos o voto é negado. 

    O funcionamento da função:

    utilizando como auxílio a bilioteca datetime, é possível comparar a data de nascimento do usuário com o ano atual do computador, 
    desta forma comparando cada uma das situações utilizando condicionais. 

    Para a utilização desta função importe a função datetime da biblioteca datetime. 
    
    """
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade <= 15:  # menor de 15 anos
        print('VOTO NEGADO!')
    elif idade > 17 and idade < 65:  # entre 18 e 65 anos
        print('OBRIGATÓRIO')
    elif idade > 15 and idade < 18: # 16 e 17 anos
        print('OPCIONAL')
    else:
        print('OPCIONAL')  # mais de 65 anos

# Programa principal

ano = int(input('Digite o ano de nascimento: '))

voto(ano)



