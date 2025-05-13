# Lista de Preços em Tupla

listagem = ('Lápis', 1.20, 'Cardeno', 26.90, 'Caderno de Disco', 89.90, 'Mochila', 64.90, 'Lapiseira', 2.50, 'Borracha', 2, 'Livro', 35.90, 'Estojo', 9.90, 'Caneta', 3)

title = 'LISTAGEM DE PREÇOS'
print('-'*40)
print(f'{title:^40}')
print('-'*40)

for produto, preco in zip(listagem[0::2], listagem[1::2]):
    print(f'{produto.ljust(30, '.')}R${preco:>8.2f}')
print('-'*40)

# Outra forma de fazer
mens = 'LISTAGEM DE PREÇOS V2.0'
print(mens.center(40))
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos].ljust(30, ".")}R$', end = ' ')
    else: 
        print(f'{listagem[pos]:>8.2f}')