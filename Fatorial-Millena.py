# Fatorial

fact = 1
number = int(input('Digite um número: '))
n = number
print(f'{number}! = ', end = ' ')
while n > 0:
    for c in range(number, 0, -1):
        fact *=c 
        print(c, end = ' ')
        n -= 1
        print(' x ' if c > 1 else f" = {fact}", end = ' ')
print(f'\nO fatorial do número {number} é igual a {fact}!')
# coisa mais fácil do mundo usando o laço FOR