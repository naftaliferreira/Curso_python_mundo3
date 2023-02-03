""" Aprimore o Desafio 093 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. """

# Listas , dicionários e tuplas
time = list()
jogador = dict()
partidas = list()

# Entrada de dados
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    # Tratamento dos dados
    for c in range(0, total_partidas):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Responda apenas Sim ou Não')
    if resposta == 'N':
        break
# Output
print('-' * 40)
print('COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

# Menu busca 
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Não existe jogador com código {busca}!')
    else:
        print(f'    == LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('Fim do programa!')
print('     >>> Volte Sempre <<<    ')