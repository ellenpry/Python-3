# Estatísticas em Produtos

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

total = 0
mil = 0
barato = ''
menor = float('inf') #isso inicia com um número infinito
print(f'{cor['yellow']}=-=-=SuperLoja=-=-={cor["clean"]}')
while True:
    nome = str(input(f'{cor["blue"]}Nome do produto:{cor["clean"]} '))
    preco = float(input(f'{cor["blue"]}Preço:{cor["clean"]} R$'))
    total += preco
    # para não usar o float('inf'), usamos o:
    # criamos uma variavel: cont = 0
    # if cont == 1 or preco < menor:
    #   menor = preco
    #   preco = produto
    if preco < menor:
        menor = preco
        barato = nome
    if preco > 1000:
        mil += 1
    esc = str(input('Deseja continuar a compra? ')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input(f'{cor["red"]}Resposta inválida.{cor["clean"]} Deseja continuar a compra? ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'{cor["green"]}Compra Finalizada!{cor["clean"]}')
print(f'O total da compra foi de R${total:.2f}')
print(f'Com o total de {mil} produtos custando acima de R$1000.00')
print(f'O produto mais barato foi o/a {barato} que custa R${menor:.2f}')
