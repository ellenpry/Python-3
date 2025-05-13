# Maior e Menor da lista - Guanabara

valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {c}° posição: ')))
    if c == 0: 
        maior = menor = valores[c]
    else: 
        if valores[c] > maior:
            maior = valores[c]
        if valores [c] < menor:
            menor = valores[c]
print('Você digitou os valores:', end = ' ')
for v in valores:
    print(v, end = '... ') 

print(f'\nO maior valor digitado foi o {maior} na posição ', end ='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}°', end = ' ')

print(f'\nO menor valor digitado foi o {menor} na posição ', end = '')
for i, v in enumerate(valores): 
    if v == menor:
        print(f'{i}°', end = ' ')
    