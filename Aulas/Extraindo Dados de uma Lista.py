# Extraindo Dados de uma Lista

lista = []
pos5 = []
num5 = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num == 5:
        num5 += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp[0] == 'N':
        break

print(f'Foram digitados {len(lista)} números!')

print(f'Lista de valores em ordem DECRESCENTE: ', end = '')
lista.sort(reverse = True)
for v in lista:
    print(v, end = '... ')

if 5 in lista: 
    print(f'\nO valor 5 foi digitado nas posições ', end = '')
    for p, v in enumerate(lista):
        if v == 5:
            pos5.append(p)
    for p in pos5:
        print(p, end = '°... ')
else: 
    print('\nO valor 5 NÂO está na lista!')