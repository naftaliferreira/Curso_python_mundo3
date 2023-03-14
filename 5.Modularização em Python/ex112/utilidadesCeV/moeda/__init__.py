
# Funções moeda

# => Aumento 

def aumentar(preco = 0, taxa = 0, formato = False):
    result =  preco + (preco * taxa / 100)
    return result if formato is False else moeda(result)


# => Diminuindo

def diminuir(preco = 0, taxa = 0, formato = False):
    result = preco - (preco * taxa / 100)
    return result if formato is False else moeda(result)


#  => função dobro

def dobro(preco = 0, formato = False):
   result = preco * 2
   return result if not formato else moeda(result)


#  => função metade

def metade(preco = 0, formato = False):
   result = preco / 2
   return result if not formato else moeda(result)


# => função formatação de moeda
def moeda(preco = 0, moeda= 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

# função de modelos de exibição
def resumo(preco = 0, taxaAum = 10, taxaDimin = 5):
    print('=' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('=' * 40)
    print(f'PREÇO ANALISADO: \t{moeda(preco)}')
    print('-' * 40)
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print('-' * 40)
    print(f'Metade do preço: \t{metade(preco, True)}')
    print('-' * 40)
    print(f'{taxaAum}% de aumento: \t{aumentar(preco, taxaAum, True)}')
    print('-' * 40)
    print(f'{taxaDimin}% de redução: \t{diminuir(preco, taxaDimin, True)}')
    print('=' * 40)