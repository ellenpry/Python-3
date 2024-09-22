# Lista composta e análise de dados

dados = []
pesos = []
pessoas = []
cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    pesos.append(dados[1])
    cont += 1
    dados.clear()
    resp = str(input('Deseja continuar [S/N]: ')).upper().split()
    if resp[0] in 'NAO':
        break 

print(f'Ao todo, você cadastrou {cont} pessoas.')

print(f'O maior peso cadastrado foi de {max(pesos)}kg!', end = ' ')
print('O peso de ', end = '')
for p in pessoas:
    if p[1] == max(pesos):
        print(p[0], end = ' ')

print(f'\nO menor peso cadastrado foi de {min(pesos)}kg!', end = ' ')
print('O peso de ', end = '')
for p in pessoas:
    if p[1] == min(pesos):
        print(p[0], end = ' ')

    