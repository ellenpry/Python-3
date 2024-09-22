# Maior e Menor valores na Lista

lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a {cont}° posicão: ')))
print('-'*50)
print('Você digitou os valores:', end = ' ')
for v in lista: 
    print(v, end = ' ')
    
    
print(f'\nO maior valor foi o {max(lista)} nas posicões', end = ' ')
maior = max(lista)
cont_maior = lista.count(max(lista))
posicoes_maior = []
if cont_maior > 1:
    for i, v in enumerate(lista):
        if v == maior:
            posicoes_maior.append(i)
    for p in posicoes_maior:
        print(f'{p}°...', end = ' ')
    print('\n')
else:
    print(f'{lista.index(max(lista))}°')


print(f'O menor valor foi o {min(lista)} nas posições', end = ' ')
menor = min(lista)
cont_menor = lista.count(min(lista))
posicoes_menor = []
if cont_menor > 1:
    for i, v in enumerate(lista):
        if v == menor:
            posicoes_menor.append(i)
    for p in posicoes_menor:
        print(f'{p}°...', end = ' ') 
    print('\n')
else:
    print(f'{lista.index(min(lista))}°')

