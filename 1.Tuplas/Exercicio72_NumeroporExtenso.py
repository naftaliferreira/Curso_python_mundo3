# tupla com numeros por extenso

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Solicitar um número de 0 a 20 ao usuário

num = int(input('Insira um número de 0 a 20 aqui: '))
print(num)

# Verificando o tamanho da tupla. (apenas para consulta)

print(len(contagem))

# Exibindo o resultado 
print('O valor digitado é ...', end=' ')
print(contagem.index(num))
