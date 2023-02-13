""" Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou.
 O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado """

# função
def ficha(jog='<Não informado>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')



 # programa principal

name = str(input('Nome do Jogador: '))
goals = str(input('Número de gols: ')) # aqui está recebendo como string pois inteiro não aceita resposta vazia. 
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name.strip() == '':
    ficha(gol=goals)
else:
    ficha(jog=name, gol=goals)

