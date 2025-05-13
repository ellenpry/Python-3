# Tratando Valores

cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}


num = int(input(f'Digite um número [{cor['red']} 999 para PARAR {cor['clean']}]: '))
soma = num
cont = 1
while num != 999:
    num = int(input(f'Digite um número [{cor['red']} 999 para PARAR {cor['clean']}]: '))
    cont += 1
    soma += num
    if num == 999:
        cont -= 1
        soma -= num
print(f'Você digitou {cor['blue']}{cont} números{cor['clean']} e a soma entre eles é igual a {cor['purple']}{soma}{cor['clean']}!')
