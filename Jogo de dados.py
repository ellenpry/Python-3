# Jogo de dados

from random import randint
from time import sleep
jogadores = {}

for j in range(1, 5):
    jogadores[f'jogador{j}'] = randint(1, 6)

print(' Valores Sorteados '.center(30, '-'))   
for k, v in jogadores.items():
    print(f'O {k} tirou o número {v}') 
    sleep(1)
    
print(' Ranking dos Jogadores '.center(30, '-'))
cont = 0
list = []
usados = []
for k, v in jogadores.items(): # lista em ordem decrescente apenas com os valores dos dados
    list.append(v)
    list.sort(reverse = True)
    
for n in list:  # colocar em ordem com um FOR
    for k, v in jogadores.items():
        if n == v and k not in usados:
            cont += 1
            print(f'{cont}° lugar: {k} com {v}')
            sleep(1)
            usados.append(k)

# Dica do Guanabara
from operator import itemgetter # nova biblioteca
ranking = {}
ranking = sorted(jogadores.items(), key = itemgetter(1))
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True) 
# o sorted organiza do menor para o maior
# o dicionario.items() para separar em key e values
# o key = itemgetter() diz por qual item sera ordenado
# se for (0) sera pela key e se for (1) sera pelo values
# o reverse = True organiza de forma decrescente


