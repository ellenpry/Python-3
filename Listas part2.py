# Listas part.2

# brincando com listas
dados = []
dados.append('Gustavo')
dados.append(40)

pessoa = []
dados.insert(0, 'Vitória')
dados.insert(1, 27)
pessoa.append(dados[:])
print(pessoa)

# listas dentro de listas
galera = [['Ana', 30], ['Maria', 24], ['Jão', 29]]
print(galera[1][0])
print(galera[2][0])

# lista de listas
for dados in galera:
    print(dados)
    
for pes in galera:
    print(pes[0])

for idade in galera:
    print(idade[1])
    
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')
    
    
# listas e input
people = []
data = []
maior = menor = 0
for c in range(0, 3):
    data.append(str(input('Nome: ')))
    data.append(int(input('Idadde: ')))
    people.append(data[:])
    data.clear()

for p in people:
    print(f'{p[0]} tem {p[1]} anos.')
    
for p in people:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} pessoas mmaiores de idade e {menor} pessoas menores de idade!')
        
        