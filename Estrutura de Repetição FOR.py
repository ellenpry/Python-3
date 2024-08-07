# Estrutura de repetição FOR

#Contando de 1 a 10
for c in range(1, 11):
    print(c, end = ' ')
print('END!')

#Contade de trás pra frente
for c in range(10, 0, -1):
    print(c, end = ' ')
print('END!')

#Contando de 2 em 2
for c in range(0, 11, 2):
    print(c, end = ' ')
print('END!')

#Lendo valores
for c in range(0, 3):
    valor = input('Digite um valor: ')
print('END')

#Somando valores
s = 0
for c in range(0, 3):
    v = int(input('Digite um valor: '))
    s += v
print(f'A somas dos valores é igual a {s}!')
print('END!')

#Escolhando ate onde a contagem vai
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    print(c, end = ' ')