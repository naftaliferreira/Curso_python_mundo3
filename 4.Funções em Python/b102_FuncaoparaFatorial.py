""" Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a 
calcular e outro chamado show,que será um valor lógico (opcional) indicando se será mostrado 
ou não na tela o processo de cálculo do fatorial."""

# função 

def fatorial(n, show=False):
    """ 
    -> Calcula o fatorial de um número: 

        * Parâmetro n: Número inteiro a ser calculado o seu fatorial.  
        * Parâmetro show: função (OPCIONAL) que permite exibir ou não a conta
        * Return: O valor do fatorial de um número n. 
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# programa principal

n = int(input('Digite o número para saber seu fatorial: '))
print(fatorial(n))

