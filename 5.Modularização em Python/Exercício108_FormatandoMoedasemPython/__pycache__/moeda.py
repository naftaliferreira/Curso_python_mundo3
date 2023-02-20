
# Funções moeda

# => Aumento 

def aumentar(preco = 0, taxa = 0):
    result =  preco + (preco * taxa / 100)
    return result


# => Diminuindo

def diminuir(preco = 0, taxa = 0):
    result = preco - (preco * taxa / 100)
    return result


#  => função dobro

def dobro(preco = 0):
   result = preco * 2
   return result


#  => função metade

def metade(preco = 0):
   result = preco / 2
   return result


# => função moeda
def moeda(preco = 0, moeda= 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

