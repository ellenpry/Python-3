# Alinhamneto Milenar

# Adicionando cores
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

from datetime import date
ano_nasc = int(input('Digite seu ano de nascimneto: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'{cor["pink"]}Você tem {idade} anos em {ano_atual}!{cor['clean']}')
if idade < 18:
    ano_alis = 18 - idade + ano_atual
    print(f'{cor["yellow"]}Ainda não é o momneto!{cor['clean']} Você irá se alistar em {cor['yellow']}{ano_alis}{cor['clean']}.')
elif idade == 18:
    print(f'{cor['green']}Está na hora!{cor['clean']} Se aliste no serviço militar imediatamnete!')
else:
    ano_alis = ano_atual - (idade - 18)
    print(f'{cor['red']}Passou da hora!{cor['clean']} Você daveria ter se alistado desde {cor['red']}{ano_alis}{cor['clean']}!')