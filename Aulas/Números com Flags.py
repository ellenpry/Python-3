# Números com Flags

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

cont = soma = 0
while True:
    num = int(input(f'Digite um valor {cor["red"]}[ 999 para parar ]{cor["clean"]}: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'{cor["blue"]}A soma entre os {cont} valores é igual a {soma}!{cor['clean']}')

    
