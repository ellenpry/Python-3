# Matriz em python

matriz = [[], [], []]
cont = 0
while len(matriz[2]) < 3:
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{cont}, {c}]: '))
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
    