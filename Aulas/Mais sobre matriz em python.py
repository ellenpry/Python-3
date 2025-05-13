# Mais sobre matriz em python

matriz = [[], [], []]
linha = []
pares = coluna = cont = 0
while len(matriz[2]) < 3:
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{cont}, {c}]: '))
        if valor % 2 == 0: # soma dos valores pares
            pares += valor
        if c == 2: # soma da terceira coluna
            coluna += valor
        if cont == 1: # maior numero da segunda linha
            linha.append(valor)
        matriz[cont].append(valor)
        if len(matriz[cont]) == 3:
            cont += 1
            
text = 'Matriz'
print(f'{text.center(15, '-')}')
c = vz = 0
while True:
    for v in matriz[c]:
        print(f'[ {v} ]', end = '')
        vz += 1 # a cada 3 valores a linha é quebrada
        if vz % 3 == 0:
            print( )
    c += 1
    if c == 3:
        break
print('-'*15)

print(f'A soma dos valores pares é igual a {pares}.')   
print(f'A soma dos valores da terceira coluna é igual a {coluna}.')
print(f'O maior valor da segunda linha é {max(linha)}.')
