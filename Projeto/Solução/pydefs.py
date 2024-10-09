# funções do projeto

cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}


def titulo(msg):
    print('-'*30)
    print(msg.center(30))
    print('-'*30)
    
    
def painel():
    titulo('MENU PRINCIPAL')
    print(f'''{cor["yellow"]}1 - {cor['purple']}Ver Pessoas Cadastradas
{cor['yellow']}2 - {cor["purple"]}Cadastrar Nova Pessoa
{cor['yellow']}3 - {cor["purple"]}Sair do Sistema{cor["clean"]}''')
    print('-'*30)
    
    
   
def entrada():
    file = 'pessoas.txt'
    painel()
    while True:
        try:
            entrada = int(input(f'{cor["yellow"]}Sua opção: {cor['clean']}'))
            if entrada > 3 or entrada == 0:
                print(f'{cor['red']}ERRO! Digite uma opção válida.{cor["clean"]}')
                painel()
            elif entrada == 1:
                titulo('PESSOAS CADASTRADAS')
                ver(file)
            elif entrada == 2:
                titulo('CADASTRAR NOVA PESSOA')
                nome = input('Nome: ')
                idade = input('Idade: ')
                cadastro(file, nome, idade)
            else:
                titulo('Saindo do Sistma... Até logo!')
                return
        except(ValueError, TypeError):
                print(f'{cor["red"]}ERRO: por favor, digite um número inteiro válido.{cor["clean"]}')


def createfile(arquivo):
    try:
        file = open(arquivo, 'wt+')
        file.close()   
    except:
        print(f'Ocorreu um erro ao abrir o arquivo {arquivo}.')
    else:
        print(f'Arquivo {arquivo} aberto com sucesso com sucesso!')
        open(arquivo, 'rt')
        
        
def cadastro(arquivo, nome = 'desconhecido', idade = 0):
    try:
        file = open(arquivo, 'at+')  
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            file.write(f'{nome};{idade}\n')
            file.close()
        except:
            print('Erro ao adicionar os dados ao arquivo.')
        else:
            print('Dados adicionados com sucesso!')
        
        
def ver(arquivo):
    r = open(arquivo, 'rt')
    for linha in r:
        dados = linha.split(';')
        dados[1] = dados[1].replace('\n', '')
        print(f'{dados[0]:<20}{dados[1]:>3} anos')
    r.close()           
            
            
        


