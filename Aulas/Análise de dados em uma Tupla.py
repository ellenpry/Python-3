# Análise de dados em uma Tupla


tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
print(f'Você digitou os valores:', end = ' ')
for n in tupla: 
    print(n, end = ' ')
# if 9 in tupla:                   # fiz muito embolado
#     cont = tupla.count(9)
print(f'\nO número 9 foi digitado {n.count(9)} vezes!')
if 3 in tupla:
    print(f'O valor 3 foi digitado na {tupla.index(3) + 1}° posição!')
else: 
    print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram:', end = ' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end = ' ')
# if tupla[0] % 2 == 0:
#     print(tupla[0], end = ' ')
# if tupla[1] % 2 == 0:
#     print(tupla[1], end = ' ')      # também fiz muito embolado
# if tupla[2] % 2 == 0:
#     print(tupla[2], end = ' ')
# if tupla[3] % 2 == 0:
#     print(tupla[3])

    

