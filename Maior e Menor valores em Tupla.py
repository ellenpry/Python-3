# Maior e Menor valores em Tupla

from random import randint
# tupla = ()
# list = []
# cont = 0
# while True:
#     gerar = randint(0, 10)
#     list.append(gerar)
#     cont +=1
#     if cont == 5:
#         break
# tupla = list
# print(f'Os valores sorteados foram: {tupla}')
# print(f'O maior valor foi {max(tupla)}!')
# print(f'O menor valor foi {min(tupla)}!')

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'O valores sorteados foram:', end = ' ')
for n in tupla:
    print(n, end = ' ')
print(f'\nO maior valor foi {max(tupla)}!')
print(f'O menor valor foi {min(tupla)}!')