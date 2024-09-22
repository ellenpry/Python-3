# Função que calcula a área

def area(l, c):
    a = l * c
    print(f'A área do seu terreno {l}x{c} é de {a:.1f}m².')
    
def titulo(text):
    print('-'*30)
    print(f'{text:^30}')
    print('-'*30)

titulo('Controle de Terrenos')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)

