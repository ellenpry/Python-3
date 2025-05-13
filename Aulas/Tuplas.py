# Tuplas
# AS TUPLAS SÃO IMUTÁVEIS

# Armazena strings enumeradas
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#              0          1        2       3
# Munipulando strings
print(lanche[2])

# O fatiamento ignora o último número
print(lanche[0:2])

# Começa na string 1 e vai até o fim
print(lanche[1:])

# Última string
print(lanche[-1])

# Quantas strings
print(len(lanche))

# Utilizando o FOR
for c in lanche:
    print(c)