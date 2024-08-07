# Estrutura de Repetição WHILE

resposta = 'Sim'
while resposta == 'Sim': # é preciso definir a variável
    valor = str(input('Digite um valor: '))
    resposta = str(input('Quer continuar? ')).title()
print('Fim!')

num = 1
par = impar = 0 # dá pra fazer assim (as duas variaveis estão com o valor 0)
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares!')
print('Fim!')
