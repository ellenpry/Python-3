# Jogo da Adivinhação 2.0

from random import randint
pc = randint(0, 10)
print('Vamos brincar de adivinhação! Você vs Computador!')
print('O computador vai "pensar" em um número. Tente adivinhar!')
cont = 0
player = 0
while pc != player:
    player = int(input('Digite um número inteiro entre 0 e 10: '))
    if player != pc:
        print('Escolha errada! Tente novamente!')
        cont += 1
print(f'Depois de {cont + 1} tentativas... \nVocê ACERTOU!')
print(f'O número pensado foi o {pc}!')
