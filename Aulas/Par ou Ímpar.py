# Par ou Ímpar

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

from random import randint

cont = soma = 0
print(f'{cor['yellow']}Vamos jogar Par ou ímpar?{cor['clean']} ')
while True:
    esc = str(input('Você escolhe par ou ímpar? [P/I] ')).strip().upper()[0]
    while esc not in 'PI':
        esc = str(input(f'{cor['red']}Resposta inválida.{cor["clean"]} Você escolhe par ou ímpar? [P/I] ')).strip().upper()[0]
    usu = int(input('Digite um número: '))
    pc = randint(0, 10)
    soma = usu + pc
    if esc == 'P':
        if soma % 2 == 0:
            cont += 1
            print(f'{cor["green"]}VOCÊ VENCEU!{cor["clean"]}')
            print(f'{cor["blue"]}Você jogou {usu} e o computador {pc}! Deu {soma} e é PAR!{cor["clean"]}')
            print(f'{cor["yellow"]}Vamos jogar novamente...{cor['clean']}')
        else:
            print(f'{cor["red"]}VOCÊ PERDEU!{cor["clean"]}')
            print(f'{cor["blue"]}Você jogou {usu} e o computador {pc}! Deu {soma} e é ÍMPAR!{cor["clean"]}')
            break
    elif esc == 'I':
        if soma % 2 != 0:
            cont += 1
            print(f'{cor["green"]}VOCÊ VENCEU!{cor["clean"]}')
            print(f'{cor["blue"]}Você jogou {usu} e o computador {pc}! Deu {soma} e é ÍMPAR!{cor["clean"]}')
            print(f'{cor["yellow"]}Vamos jogar novamente...{cor["clean"]}')
        else:
            print(f'{cor["red"]}VOCÊ PERDEU!{cor["clean"]}')
            print(f'{cor["blue"]}Você jogou {usu} e o computador {pc}! Deu {soma} e é PAR!{cor["clean"]}')
            break
print(f'{cor["yellow"]}Game over! Você venceu {cont} vezes!{cor["clean"]}')
 
    