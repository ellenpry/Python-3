# Validações Expressões Matemáticas


exp = input('Digite uma expressão: ')
lista = list(exp)
print(lista)
cont1 = exp.count('(')
cont2 = exp.count(')')
if cont1 == cont2:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
print(cont1, cont2)