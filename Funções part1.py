# Funções part1

def linha():  # eh tipo criar um comando novo
    print('-'*30)
    
linha()
print(f'{'Curso em Vídeo':^30}')
linha()


def mensagem(msg):  # dentro dos parenteses fica a variavel que vc quer declarar
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)
mensagem('Python') # serve como parametro para essa variavel


# def dentro de def
def frase(frs):
    linha()
    print(f'{frs:^30}')
    linha()
frase('Lily e Kali')

# somando
def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma A + B = {a + b}')
soma(4, 5)
linha()
soma(a = 8, b = 6) # posso especificar
linha()
soma(b = 2,  a = 1) # posso inverter os valores

def contador(* num):  # com o uso do * ele guarda os valores em 'num' e os transforma em uma tupla (desempacotar)
    print(num)
contador(2, 4, 8)
contador(1, 3, 5, 7, 9)  

def contar(* number):    # posso tratar igual uma tupla
    for valor in number:
        print(valor, end = ' ')
    print('Fim!')
contar(2, 4, 6, 8)
contar(1, 0, 7, 9, 11)

def dobra(lista):  # def e lista
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
valores = [2, 7, 1, 0, 4]
dobra(valores)  # dobrei os valores da lista
for v in valores:
    print(v, end = ' ')
print()

# somando valores
def somar( * valores):
    s = 0
    for v in valores:
        s += v
    print(f'A soma dos valores {valores} é igual a {s}')
somar(2, 5, 7, 1, 9, 0, 3)

