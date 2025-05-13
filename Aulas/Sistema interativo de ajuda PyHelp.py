# Sistema interativo de ajuda PyHelp

from time import sleep

cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

def titulo(texto):
    print('-' * len(texto))
    if texto in ' PROGRAMA ENCERRADO! ':
        print(cor['red'], texto, cor['clean'])
    else:
        print(cor['pink'], texto, cor['clean'])
    print('-' * len(texto))
    
def pyhelp(comando):
    texto = f'Acessando o Manual do Comando "{comando}" '
    print('-' * len(texto))
    print(cor['green'], texto, cor['clean'])
    print('-' * len(texto))
    sleep(0.5)
    help(comando)

while True: 
    titulo('SISTEMA DE AJUDA PYHELP ')
    comd = str(input('Digite uma Funcão ou Biblioteca: '))
    if comd in 'FimfimFIM':
        break
    pyhelp(comd)
    sleep(1)
titulo('PROGRAMA ENCERRADO! ')
