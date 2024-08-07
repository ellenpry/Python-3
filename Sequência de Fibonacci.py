# Sequência de Fibonacci

cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

list = []
num = int(input('Digite um número: '))
print(f'Os {num} primeiros valores da sequência de fibonacci: ')
while len(list) < 10:
    for c in range(0, num + 1):
        list.append(c)
    pen = list[-2]
    print(max(list) + pen)

    # print(cor['red'], c + fib, cor['clean'])