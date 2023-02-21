
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


# => função moeda
def moeda(preco = 0, moeda= 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')



