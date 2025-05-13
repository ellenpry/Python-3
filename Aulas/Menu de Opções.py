# Menu de Opções

# Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
opcao = 0
list = []
while opcao != 5:
    print(f'{cor['yellow']}Carregando...{cor['clean']}')
    sleep(1)
    print(f'''Menu de Opções: Escolha uma opção abaixo
      {cor['blue']}[1] Somar
      [2] Multiplicar
      [3] Maior Valor
      [4] Novos Valores
      [5] Sair do Programa{cor['clean']}''')
    opcao = int(input('Digite aqui: '))
    if opcao == 1:
        print(f'A soma entre os números {v1} e {v2} é igual a {cor['green']}{v1 + v2}{cor['clean']}!')
    elif opcao == 2:
        print(f'O produto entre os números {v1} e {v2} é igual a {cor['green']}{v1 * v2}{cor['clean']}!')
    elif opcao == 3:
        list.append(v1)
        list.append(v2)
        print(f'O maior número digitado foi o {cor["green"]}{max(list)}{cor['clean']}!')
    elif opcao == 4:
        print('Digite abaixo 2 novos valores:')
        for valor in range(0, 1):
            
            v1 = int(input('1° valor: '))
            v2 = int(input('2° valor: '))
            list.clear()
    elif opcao > 5:
        print(f'{cor['red']}Opção invalida! Tente novamente!{cor['clean']}')
print(f'{cor['red']}Fim do programa!{cor['clean']}')        
            