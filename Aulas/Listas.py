# Listas 

lanche = ['Hamburguer', 'Pizza', 'Pudim', 'Suco']
print(lanche) #Resultado = ['Hamburguer', 'Pizza', 'Pudim', 'Suco']

# as listas são mutáveis
lanche[3] = 'Picolé'
print(lanche) #Resultado = ['Hamburguer', 'Pizza', 'Pudim', 'Picolé']

# adicionando elementos no final da lista
lanche.append('Macarrão')
print(lanche) #Resultado = ['Hamburguer', 'Pizza', 'Pudim', 'Picolé', 'Macarrão']

# adicionando elementos em um lugar especifico da lista
lanche.insert(0, 'Bolo') # .insert(posição, elemento)
print(lanche) #Resultado = ['Bolo', 'Hamburguer', 'Pizza', 'Pudim', 'Picolé', 'Macarrão']

# removendo elementos da lista
del lanche[0] 
lanche.pop(0) #remove pelo indice
lanche.pop #remove o último elemento
lanche.remove('Pizza') #remove pelo conteudo
print(lanche)

#adicionando valores do range em uma lista
valores = list(range(4, 11))
print(valores)

#colocando uma lista em ordem
numeros = [1, 5, 7, 3, 8, 8, 0]
numeros.sort()
print(numeros)

#colocando a lista em ordem decrescente 
numeros.sort(reverse = True)
print(numeros)

# brincando com as estruturas
valores = []
valores.append(0)
valores.append(5)
valores.append(2)
valores.append(1)
print('Os valores são:', end = ' ')
for v in valores:
    print(v, end = ' ')
print('\n')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for p, v in enumerate(valores): 
    print(f'Na posiçãO {p}° encontrei o valor {v}!')
print('Cheguei ao final da lista!')

# ligação entre listas
a = [2, 4, 6, 8]
b = a # isso é uma ligação. se eu mudar a list.b, a list.a tambe muda
b[2] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# copiar uma lista
a = [2, 4, 6, 8]
# para nao interligar as listas, nos usamos o fatiamento
b = a[:] # fatiando todos os elementos da lista
b[2] = 7 # vai mudar apenas a list.b
print(f'Lista A: {a}')
print(f'Lista B: {b}')
