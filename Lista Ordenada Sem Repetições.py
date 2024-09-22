# Lista Ordenada Sem Repetições

valores = []
num = int(input('Digite um valor: '))
valores.append(num)
print('Adicionado ao final da lista...')

for c in range(0, 4):
    num = int(input('Digite um valor: '))
    
    
    if num > max(valores):
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if num <= valores[posicao]:
                valores.insert(posicao, num)
                print(f'Adicionado na posição {posicao}° da lista...')
                break
            posicao += 1
print('-=-'*20)
print('Os valores digitados em ordem: ', end = '')
for n in valores:
    print(n, end = ' ')
        