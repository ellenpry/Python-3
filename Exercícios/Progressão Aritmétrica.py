# Progressão Aritmétrica
resp = 'Sim'

num = int(input('Digite um número inteiro: '))
print(f'Os primeiros 10 valores da P.A({num}): ')
for c in range(num, num * 11, num):
    print(c, end =' → ')
    
while resp == 'Sim':
    print('Carregando...')
    resp = str(input('Deseja continuar com a progressão? ')).title()
    if resp == 'Sim':
        newnum = int(input('Digite o número de valores a mais que deve ser mostrado: '))
        print(f'Os primeiros {newnum + 10} valores da P.A({num}): ')
        for n in range(num, num * (newnum + 11), num):
            print(n, end = ' → ')
print('Fim da Progressão!')