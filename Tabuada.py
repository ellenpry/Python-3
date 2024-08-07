# Tabuada

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

number = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{number} x {c:2} = {number * c}')