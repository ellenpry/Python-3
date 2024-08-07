# Tabuada v2.0

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

while True:
    num = int(input(f'Quer ver a tabuada de qual número? '))
    print('-=-' * 13)
    if num < 0:
        break
    for n in range(1, 11):
        print(f'{cor["blue"]}{num} x {n:2} = {num * n}{cor["clean"]}')
    print('-=-' * 13)
print(f'{cor['red']}Programa Encerrado!{cor['clean']}')
    