# Ficha de jogador

def ficha(nome, gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = 0  
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato!')

def linha():
    print('-'*30)

linha()
name = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
ficha(name, gols)
linha()
