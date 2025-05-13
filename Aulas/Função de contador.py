# Função de contador

from time import sleep

def linha():
    print('-'*50)

def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = abs(passo)
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    
    if fim < inicio:
       for c in range(inicio, fim - 1, -passo):  # decrescente
        print(c, end = '... ', flush = True) 
        sleep(0.5)
    else:
        for c in range(inicio, fim + 1, passo):  # crescente
            print(c, end = '... ', flush = True) # o flush força a saida
            sleep(0.5)
    print('Fim!')

linha()
contagem(1, 10, 1) # primiera contagem
linha()

contagem(10, 0, 2) # segunda contagem
linha()

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contagem(inicio, fim, passo) # terceira contagem
linha()