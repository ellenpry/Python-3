# Cadastro de jogadores de futebol

jogador = {}
gol = []
soma = 0

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0, partidas):
    gol.append(int(input(f'Quantos gols na {c + 1}° partida? ')))
    soma += gol[c]
jogador['gols'] = gol.copy()
jogador['total'] = soma   # ou sum(gol) que é igual a soma dos valores da list gol

print()
print(jogador)
print()

for k, v in jogador.items():
    print(f'O campo {k.title()} tem o valor {v}.')
print()

print(f'O jogador {jogador['nome']} jogou {partidas} partidas!')
for i, g in enumerate(gol):
    print(f' → Na {i + 1}° partida fez {g} gol(s)')
print(f'Ao todo com um total de {jogador['total']} gols.')
