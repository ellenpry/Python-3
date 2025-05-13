# lista e dicionarios

# brasil = []
# e1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# e2 = {'Uf': 'Pernambuco', 'sigla': 'PE'}
# brasil.append(e1)
# brasil.append(e2)
# print(brasil[0]['uf'])

brasil = []
estado = {}
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end = ' ')
    print()