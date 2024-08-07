# Simulador de Caixa Eletrônico

print('-=-=-=-=MiBank=-=-=-=-')

valor = int(input('Qual valor deseja sacar? R$'))
c50 = valor // 50
if c50 > 0:
    print(f'Total de {c50} cédulas de R$50')
valor = valor % 50
c20 = valor // 20
if c20 > 0:
    print(f'Total de {c20} cédulas de R$20')
valor = valor % 20
c10 = valor // 10
if c10 > 0:
    print(f'Total de {c10} cédulas de R$10')
valor = valor % 10
c1 = valor
if c1 > 0:
    print(f'Total de {c1} cédulas de R$1')

print('-=-=-=-=-=-=-=-=-=-=-=-')
print('Volte sempre ao MiBank!')

# Usando o WHILE
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
v = int(input('Valor: R$'))
ced = 50
total = v
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        print(f'Total de {contced} cédulas de R${ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break
        
        
        
        
    
