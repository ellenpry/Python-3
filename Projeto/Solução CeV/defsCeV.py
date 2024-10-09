# resposta

from time import sleep

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
        
        
 
def findfile(nome): # verifica se existe o arquivo
    try:
        a = open(nome, 'rt')    # tenta abrir o arquivo em modo de leitura read text
        a.close()
    except FileNotFoundError: # se der erro ele retorna false, se der certo ele retorna true
        return False
    else:
        return True



def createfile(arquivo): # cria um arquivo
    try:
        open(arquivo, 'wt+') # abre o arquivo no modo write text (esse + é pra criar caso nao exista // faz toda a diferença)
    except:
        print(f'Ocorreu um erro ao criar o arquivo {arquivo}.')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!') 
        

def readfile(nome): # ler o arquivo
    try:
        a = open(nome, 'rt') # tenta abrir no mode read
    except:
        print('Erro ao ler arquivo!') 
    else:
        titulo('PESSOAS CADASTRADAS') # se der certo, mostra o titulo e printa o arquivo com a função read
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<25}{dados[1]:>3} anos')
    finally:
        a.close()
        

def writefile(file, nome = 'Desconhecido', idade = 0):
    try:
        a = open(file, 'at+')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            a.close()
        except:
            print('Erro ao adicionar os dados. Tente novamente!')
        else:
            print(f'{nome} registrado(a) com sucesso!')

        
        
                   
                
def titulo(msg):
    print('-'*35)
    print(msg.center(35))
    print('-'*35)
  
    
    
def painel(lista):
    titulo('MENU PRINCIPAL') # menu do sistema
    cont = 1
    for item in lista:  # receba uma lista e separa direitinho com o for
        print(f'{cor["yellow"]}{cont} - {cor["purple"]}{item}{cor["clean"]}')
        cont += 1
    opc = leiaint('Sua opção: ') # chama o leiaint e verifica se é um numero inteiro
    return opc # retorna o numero
        
