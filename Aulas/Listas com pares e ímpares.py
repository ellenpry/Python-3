# Listas com pares e ímpares

valores = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}° valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(valores)

print('Os valores pares digitados foram: ', end = '')
valores[0].sort()
for v in valores[0]:
    print(v, end = ' ')

print('\nOs valores ímpares digitados foram: ', end = '')
valores[1].sort()
for v in valores[1]:
    print(v, end = ' ')
    