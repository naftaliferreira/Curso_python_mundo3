
# Funções moeda

#  => função dobro

def dobro(n):
    dobro = n*2
    print(f'O dobro de {n} é ${dobro}') 
    return

#  => função metade

def metade(n):
    metade = n/2
    print(f'A metade de {n} é ${metade}')


# => Aumento 

def aumento(n):
    percent = int(input('Percentual do aumento: '))
    aumento = ((n * percent) / 100) + n
    print(f'Aumentando {percent}% é  ${aumento}')


# => Diminuindo

def diminuindo(n):
    percent = int(input('Percentual do desconto: '))
    dimin = n - ((n * percent) / 100)
    print(f'Diminuindo {percent}% é ${dimin}')

