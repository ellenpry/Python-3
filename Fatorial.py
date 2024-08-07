# Fatorial

fact = 1
number = int(input('Digite um número: '))
for c in range(number, 0, -1):
    fact *=c
print(f'O fatorial do número {number} é igual a {fact}!')
# coisa mais fácil do mundo usando o laço FOR