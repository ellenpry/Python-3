# Progressão Aritmétrica
resp = 'S'

num = int(input('Digite um número inteiro: '))
raz = int(input('Digite a razão da P.A: '))
print(f'Os primeiros 10 valores da P.A({num}, {raz}): ') 
for c in range(num, (raz * 10) + num, raz):
    print(c, end =' → ')
    
while resp == 'S':
    print('Carregando...')
    resp = str(input('Deseja continuar com a progressão? ')).strip().upper()[0]
    if resp == 'S':
        newnum = int(input('Digite o número de valores a mais que deve ser mostrado: '))
        print(f'Os primeiros {newnum + 10} valores da P.A({num}, {raz}): ')
        for n in range(num, raz * (newnum + 10) + num, raz):
            print(n, end = ' → ')
print('Fim da Progressão!')