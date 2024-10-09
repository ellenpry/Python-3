
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}


from time import sleep
from defsCeV import painel, titulo, findfile, createfile, readfile, writefile


# Programa principal

file = 'pyarquivo.txt'
if not findfile(file):
    createfile(file)
    

while True:
    resposta = painel(['Criar Arquivo', 'Cadastrar Pessoa', 'Listar Pessoas', 'Sair do Sistema'])
    print(f'Resposta recebida: {resposta}')
    if resposta == 1:
        titulo('OPÇÃO 1')
    elif resposta == 2:
        titulo('CADASTRAR PESSOAS')
        nome = str(input('Nome: '))
        idade = input('Idade: ')
        writefile(file, nome, idade)
    elif resposta == 3:
        readfile(file)
    elif resposta == 4:
        titulo('Saindo do Sistema... Até logo!')
        break
    else:
        print(f'{cor["red"]}ERRO! Digite uma opção válida!{cor["clean"]}')
    sleep(1.5)    