"""Crie um programa onde o usuário digite uma expressão qualquer que use 
parênteses. Seu aplicativo deverá analisar se a expressão passada está com 
os parênteses abertos e fechados na ordem correta.  """


# Insirindo expressões matemáticas

Expressao = str(input('Digite uma expressão: '))

# Tratando as expressões
pilha = []
# Laço para verificar a expressão, sempre que abre as aspas é armazenado na pilha, somente é removido quando inserido o fechamento de aspas

for simbolo in Expressao: 
    
    if simbolo == '(':
        pilha.append('(')
    
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop() # se a pilha estiver > 0, é para apagar. 
        else:
            pilha.append(')')
            break
# Resultado       
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')

