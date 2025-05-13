# Palpites para a Mega Sena

print('-'*40)
print('MEGA SENA'.center(40))
print('-'*40)

res = int(input('Digite quantos jogos você quer sortear: '))

print('='*40)
print(f'SORTEANDO {res} JOGOS'.center(40))
print('='*40)

from random import randint
from time import sleep
jogos = []
numeros = []
cont = 0

while True:
    while len(numeros) < 6:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    cont += 1
    if cont == res:
        break

for c in range(0, res):
    jogos
    print(f'Jogo {c + 1}: {jogos[c]}')
    sleep(1)