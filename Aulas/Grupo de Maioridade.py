# Grupo de Maioridade

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for people in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimneto da {people}° pesssoa: '))
    age = atual - nasc
    if age >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já alcançaram a maior idade e {menor} pessoas ainda são menor de idade!')