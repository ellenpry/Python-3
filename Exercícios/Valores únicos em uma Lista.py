# Valores únicos em uma Lista

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

valores = []

while True:
    num = int(input(f'{cor["blue"]}Digite um valor: {cor["clean"]}'))
    if num not in valores:
        valores.append(num)
        print(f'{cor["green"]}Valor adicionado com sucesso...{cor["clean"]}')
    else: 
        print(f'{cor["red"]}Valor duplicado! Não vou adicionar...{cor["clean"]}')
    esc = str(input(f'Deseja continuar? [S/N] ')).upper().strip()
    if esc[0] == 'N':
        break
print('-=-'*15)
print(f'Você digitou os valores: ', end = '')
valores.sort()
for v in valores:
    print(f'{cor["pink"]}{v}', end = ' ')
print(f'{cor["clean"]}')