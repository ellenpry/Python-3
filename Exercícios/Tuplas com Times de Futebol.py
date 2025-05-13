# Tuplas com Times de Futebol

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

times = ('Botafogo', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Cruzeiro', 'São Paulo', 'Bahia', 'Athletico-PR', 'Atlético-MG', 'Bragantino', 'Vasco', 'Criciúma', 'Juventude', 'Grêmio', 'Vitória', 'Internacional', 'Fluminense', 'Corinthians', 'Cuiabá', 'Atlético-GO')

print(f'''Os 5 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol: 
      {cor["blue"]}{times[0:5]}{cor["clean"]}''')
print('-=-' * 25)
print(f'''Os últimos 4 colocados da Tabela do Campeonato Brasileiro de Futebol: 
      {cor["blue"]}{times[-4:]}{cor["clean"]}''')
print('-=-'*25)
print(f'''Lista com os times em ordem alfabética: 
      {cor["blue"]}{sorted(times)}{cor["clean"]}''')
print('-=-'*25)

esc = str(input('Escolha um time entre o 20 primeiros classificados do Brasileirão: ')).title()
print(f'{cor["blue"]}O time {esc} está em {times.index(esc) + 1}° lugar na Tabela do Campeonato Brasileiro de Futebol!{cor["clean"]}')
