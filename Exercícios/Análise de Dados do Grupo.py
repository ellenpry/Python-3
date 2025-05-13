# Análise de Dados do Grupo

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

man = 0
wom = 0
total = 0
while True:
    print(f'{cor['yellow']}CADASTRE UMA PESSOA{cor["clean"]}')
    idade = int(input(f'{cor['blue']}Idade:{cor['clean']} '))
    if idade > 18:
        total += 1
    sexo = str(input(f'{cor['blue']}Sexo [F/M]:{cor['clean']} ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input(f'{cor['blue']}Sexo [F/M]:{cor['clean']} ')).strip().upper()[0]
    if sexo == 'M':
        man += 1
    elif sexo == 'F':
        if idade < 20:
            wom += 1
    esc = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]
    while esc not in 'SN':
       esc = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0] 
    if esc == 'N':
        break
print(f'{cor['red']}FIM DO PROGRAMA!{cor['clean']}')
print(f'Total de pessoas maiores de 18 anos: {total}')
print(f'Ao todo temos {man} homens cadastrados e {wom} mulheres com menos de 20 anos!')

# Ta parecendo uma gambiarra!