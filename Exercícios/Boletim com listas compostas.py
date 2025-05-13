# Boletim com listas compostas

alunos = []
dados = []
medias = []
from time import sleep

while True:
    dados.append(str(input('Nome: ')))  
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    dados.append(n1)
    dados.append(n2)  # adiciando as notas em uma lista temporaria
    
    m = (n1 + n2) / 2  # colocando as media em uma lista
    medias.append(m)
    
    res = str(input('Deseja continuar? [S/N] ')).upper().split() 
    alunos.append(dados[:]) # lista de alunos, cada aluno tem uma lista com as notas
    dados.clear()
    if res[0] in 'NAO':
        break
print('-'*30)  

print(f'{'N°':<4}{'NOME':<10}{'MÉDIA':>7}')

for c in range(0, len(alunos)):   # range para mostrar a tabela de medias
    print(f'{c:<4}{alunos[c][0]:<10}{medias[c]:>7.1f}')
print('-'*30)  

print('Digite o número que corresponde ao aluno!')
opc = 0
while opc != 999:   # while para escolher o aluno
    opc = int(input('Mostrar notas de qual aluno? [999 INTERROMPE] '))
    for a in alunos: 
        if opc == alunos.index(a):
            print(f'As notas de {a[0]} são {a[1]} e {a[2]}')
print('FINALIZANDO...')
sleep(1)
print(' VOLTE SEMPRE '.center(30, '-'))
