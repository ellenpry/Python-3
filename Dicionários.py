# Dicionários

dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome']) #res: Pedro

# criar um elemento
dados['sexo'] = 'M' 
print(dados)  #res: {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}

# apagar um elemento
del dados['sexo']
print(dados)  #res: {'nome': 'Pedro', 'idade': 25}

# dicinario de filmes
filmes = {'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'
}
print(filmes.values())  # mostra apenas os valores do dicionario
#res: dict_values(['Star Wars', 1977, 'George Lucas'])

print(filmes.keys())  # mostra apenas as chaves do dicionario
#res: dict_keys(['titulo', 'ano', 'diretor'])

print(filmes.items())  # mostra os valores e as chaves do dicionario
#res: dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

# dicionarios e FOR
for k, v in filmes.items():
    print(f'O {k} é {v}')
#res: O titulo é Star Wars
#     O ano é 1977
#     O diretor é George Lucas

