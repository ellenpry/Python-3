# Validando Expressões Matemáticas - Guanabara

exp = str(input('Digite uma expressão matemática: '))
pilha = []
for simbolo in exp:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbolo)
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é ínvalida!')
        
