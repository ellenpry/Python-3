# Números Primos 

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

cont = 0
number = int(input('Digite um número: '))
for c in range(1, number + 1):
    if number % c == 0:
        print(cor['red'], end = ' ')
        cont += 1      
    else:
        print(cor['clean'], end = ' ')
    print(c, cor['clean'], end = ' ')
if cont == 2:
    print(f'\n Foi dividido {cont} vezes. ')
    print(f'O número {cor['blue']}{number}{cor['clean']} é {cor['green']}PRIMO{cor['clean']}!')
else:
    print(f'\n Foi dividido {cont} vezes.')
    print(f'O número {cor['blue']}{number}{cor['clean']} {cor['red']}NÃO É PRIMO{cor['clean']}!')
    
