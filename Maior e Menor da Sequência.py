# Maior e Menor da Sequência

list = []
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    list.append(peso)
maior = max(list)
menor = min(list)
print(f'O maior peso lido foi de {maior}Kg e o menor foi de {menor}Kg!')