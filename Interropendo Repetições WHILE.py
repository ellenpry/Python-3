# Interropendo repetições WHILE

# O "while True" é um loop infinito.
# O "break" serve para sair desse loop.
cont = 1
while True:
     print(cont, end = ' → ')
     cont += 1
     if cont == 100:
         break
print(f'{cont} → Acabou!')

# Podemos usar "flags" para parar o ciclo, por exemplo:
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print(f'A soma entre os números digitados é igual a {s}!')
# O número 999 é uma flag, pois serve como uma bandeira para parar.

# Usando o comando break
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma entre os números digitados é igual a {s}!')


