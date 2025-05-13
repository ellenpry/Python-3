# Analisador Completo

soma = 0
idadevelho = 0
nomevelho = ''
cont = 0
for c in range(1, 5):
    print(f'===== {c}° PESSOA =====')
    nome = str(input('Nome: ')).title()
    idd = int(input('Idade: '))
    soma += idd
    sexo = str(input('Sexo F/M: ')).upper()
    if c == 1 and sexo == 'M':
        idadevelho = idd
        nomevelho = nome
    if sexo in 'M' and idd > idadevelho:
        idadevelho = idd
        nomevelho = nome
    if sexo == 'F' and idd < 20:
       cont += 1 
media = soma/4
print(f'O homem mais velho tem {idadevelho} anos e se chama {nomevelho}!')
print(f'A média das idades do grupo é igual a {media}!')
print(f'Ao todo são {cont} mulheres com menos de 20 anos!')
