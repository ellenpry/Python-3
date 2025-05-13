# MMM - Maior, Menor e Média 


num = int(input('Digite um número: '))
cont = 1
soma = num
list = [num]
resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    list.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = soma / cont
print(f'Você digitou {cont} números e a média foi igual a {media:.2f}!')
if min(list) == max(list):
    print('Não existe maior e menor valor! Você digitou apenas números iguais.')
else:
    print(f'O maior valor digitado foi o {max(list)} e o menor o {min(list)}!')

# Posso descobrir o maior e o menor valor usando o if:
# maior = menor = num
# if num > maior:
#     maior = num
# if num < menor:
#     menor = num
