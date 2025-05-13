# Unindo listas e dicionários
lista = []
pessoas = {}
dados = []
soma = cont = 0

while True:
    dados.append(str(input('Nome: ')))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
        if sexo == 'F' or sexo == "M":
            dados.append(sexo)
            break
        else:
            print('ERRO! Responda apenas com M para Masculino ou F para Feminino.')  
    dados.append(int(input('Idade: ')))
    soma += dados[2]  # soma para calcular as medias
    pessoas[dados[0]] = dados.copy()  # copia dos dados para um dicionario 
    lista.append(pessoas.copy()) # copia dos dicionarios para uma lista
    dados.clear()
    pessoas.clear()
    while True:
        res = str(input('Deseja continuar? [S/N] ')).upper().strip().split()
        if res[0] != 'S' and res[0] != 'N':
            print('ERRO! Responda apenas com S para Sim ou N para Não.')
        else:
            break
    if res[0] in 'NAO':
        break
print()

print(f'O grupo tem {len(lista)} pessoas.')
media = soma / len(lista)
print(f'A média das idades é de {media:.2f} anos.')
print('As mulheres cadastradas foram:', end = ' ')
for pessoa in lista:
    for dado in pessoa.values():
        if dado[1] in 'Ff':
            print(f'[{dado[0].title()}]', end = ' ')


print('\nLista de pessoas acima da média: ')
for pessoa in lista:
    for dado in pessoa.values():
        if dado[2] > media:
            print(f' → Nome = {dado[0].title()}; Sexo = {dado[1]}; Idade = {dado[2]};')
print()
