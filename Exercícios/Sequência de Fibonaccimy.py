# Sequência de Fibonacci

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

num = int(input('Quantos termos serão mostrados? '))
p = 0
s = 1
cont = 3
print(f'{p} → {s} → ', end = '')
while cont <= num:
    t = p + s
    p = s
    s = t
    cont += 1
    print(f'{t} → ', end = '')
print(f'{cor['red']}Fim!{cor['clean']}')


 
