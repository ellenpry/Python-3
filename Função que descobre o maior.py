# Função que descobre o maior

from time import sleep
def maior(* valor):
    maior = 0
    print('Números: ', end = '')
    for v in valor:
        print(v, end = ' ', flush = True)
        sleep(0.5)
        if v > maior:
            maior = v
    print(f'\nForam informados {len(valor)} valores ao todo.')
    print(f'O MAIOR valor informado foi o {maior}!')

def linha():
    print('-'*50)

linha()
maior(2, 9, 4, 5, 7, 1)  #1
linha()
maior(4, 7, 0)  #2
linha()
maior(1, 2)  #3
linha()
maior(6)  #4
linha()
maior()  #5
linha()