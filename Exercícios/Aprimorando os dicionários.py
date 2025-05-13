# Aprimorando os dicionários

jogador = {}
gol = []
jogadores = []
soma = 0

while True:
    print()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(0, partidas):
        gol.append(int(input(f'Quantos gols na {c + 1}° partida? ')))
        soma += gol[c]
    jogador['gols'] = gol.copy()
    jogador['total'] = soma
    jogadores.append(jogador.copy())
    
    jogador.clear() # limpando as variaveis
    gol.clear()
    soma = 0
    
    res = str(input('Deseja continuar? [S/N] ')).upper().split()
    if res[0] in 'NAO': 
        break
print()

print('-'*40)
print(f'{'C. Nome':<13}{'Gols':^15} {'Total':>10}')
print('-'*40)

for jogador in jogadores:
    print(jogadores.index(jogador), end = '  ')
    for key, valor in jogador.items():
        if key == 'total':
            print(f'{str(valor):>5}', end = ' ')   # coloquei um if pra deixar o total alinhado
        else:
            print(f'{str(valor):<13}', end = ' ')
    print()    
print()

esc = 0
cont = 1
print('Digite o código do jogador correspondente!')
while True:
    esc = int(input('Deseja mostrar dados de qual jogador? [999 para PARAR] '))
    if esc == 999:
        break
    cont = 1
    if esc < len(jogadores):
        print(f' LEVANTAMENTO DO JOGADOR {str(jogadores[esc]['nome']).upper()} '.center(40, '-'))
        for jogador in jogadores:
            if esc == jogadores.index(jogador):
                for key, valor in jogador.items():
                    if key == 'gols':
                        for gol in valor:
                            print(f'No {cont}° jogo fez {gol} gols.')
                            cont += 1
    else:
        print(f'ERRO! Não existe jogador com o código {esc}. Tente novamente!')                             
