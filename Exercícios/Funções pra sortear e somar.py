# Funções pra sortear e somar

from random import randint
numeros = []

def sorteio():
    for c in range(0, 5):
      num = randint(1, 10) 
      numeros.append(num)
    print('Sorteando 5 valores da lista: ', end = '')
    for n in numeros:
        print(n, end = ' ')
    
    
def soma(lista):
    s = 0
    for n in list(lista):
        if n % 2 == 0:
            s += n 
    print(f'\nSomando os valores pares de {lista}, temos {s}!')
        
# main
sorteio()
soma(numeros)