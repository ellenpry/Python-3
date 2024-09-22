# Tuplas v2

lanche = ('hambúrguer', 'espaguete', 'bombom', 'pudim')

# Testando 
print(lanche)

# Percorrendo uma tupla
for comida in lanche:
    print(f'Eu vou comer um {comida}...')
print('Comi pra caramba!')

# Utilizando o len()
for cont in range(0, len(lanche)):  # Começa no lanche[0] e percorre até o penúltimo item da tupla lanche, pois o último número sempre é ignorado!
    print(lanche[cont]) # Para cada cont será mostrado um item da tupla lanche!
    print(cont) # contagem normal 

# Posição dos itens de uma tupla
for posicao, comida in enumerate(lanche): # Adicionamos a class enumerate para mostrar a posição dos itens da tupla lanche
    print(f'Eu vou comer a comida {comida} da posição {posicao}') # Também adicionamos uma variável para receber essa posição
    
# Colocando a tupla em ordem alfabética (mas óbvio, sem mudar a tupla definitivamente, pois ela é IMUTÁVEL!)
print(sorted(lanche))

# Criando tuplas
a = (2, 4, 5, 8)
b = (3, 1, 2, 7, 4)
c = a + b # Juntando as duas tuplas em uma só
print(c)
print(len(c)) # mostra quantos itens tem a tupla 
print(c.count(2)) # mostra quantas vezes aparece o número 5
print(c.index(8)) # mostra em que posição esta o 8 na tupla
print(c.index(2, 1)) # mostra em que posição está o 2 a partir da posição 1

# Podemos ter dados de tipos diferentes na mesma tupla
dados = ('Ana', 29, 'Feminino', 48.4)
print(dados)
del(dados) # podemos apagar a tupla (o del pode apagar qualquer variável)