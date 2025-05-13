# Dividindo valores em várias listas

valores = []
par = []
impar = []
resp = 'S'
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp[0] == 'N':
        break
    elif resp[0] != 'S' and resp[0] != 'N':
        print('Resposta Inválida! Responda apenas com Sim[S] ou Não[N].')
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A Lista Completa é: {valores}')
print(f'A Lista de Números Pares é: {par}')
print(f'A Lista de Números ímpares é: {impar}')