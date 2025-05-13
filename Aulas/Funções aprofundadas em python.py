# Funções aprofundadas em python

cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}


def leiaint(msg): # recebe uma mensagem
    while True:
        try:
            valor = int(input(msg))  # a mensagem se torna um input que so aceita numeros inteiros
        except(ValueError, TypeError): # quando der erro, ele mostra a mensagem...
            print(f'{cor['red']}ERRO! Por favor, digite um valor inteiro válido!{cor['clean']}')
            continue # e volta pro começo do loop (no try)
        except(KeyboardInterrupt): # se interromper o programa, ele mostra uma mensagem...
            print(f'{cor["red"]}Úsuario preferiu não digitar esse número.{cor["clean"]}')
            valor = 0
            return valor # e retorna o valor (e quebra o loop
        else:
            return valor # der tudo certo, ele retorna o valor
 
            
def leiareal(msg):
    while True:
        try:
            real = input(msg).strip().replace(",", ".") # ele transforma a mensagem em um input e, caso tenha "," ele troca por "."
            real = float(real) 
        except(ValueError, TypeError):
            print(f'{cor['red']}ERRO! Por favor, digite um valor real válido!{cor['clean']}')
            continue
        except(KeyboardInterrupt):
            print(f'{cor["red"]}Úsuario preferiu não digitar esse número.{cor["clean"]}')
            real = 0
            return real
        else:
            return real

n1 = leiaint('Digite um número inteiro: ')
n2 = leiareal('Digite um número real: ')
print(f'{cor["blue"]}O valor inteiro digitado foi o {n1} e o real o {n2}!{cor["clean"]}')