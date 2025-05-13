# Método de Pagamento

from time import sleep
valor = float(input('Digite o valor total das compras: R$'))
print('Escolha o Método de Pagamento')
print('''1 - À vista em dinheiro/cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')
metodo = int(input('Digite aqui: '))
print('Carregando...')
sleep(1)
if metodo == 1:
    sale = valor - (valor * 0.1)
    print(f'Com o desconto de 10%, suas compras ficaram por R${sale}!')
elif metodo == 2:
    sale = valor - (valor * 0.05)
    print(f'Com um desconto de 5%, suas compras ficaram por R${sale}!')
elif metodo == 3:
    print(f'Suas compras forem divididas em 2x de R${valor/2:.2f}!')
elif metodo == 4:
    parcelas = int(input('Em quantas parcelas? '))
    if parcelas < 3:
        print('Esse método de pagamento é refente APENAS a compras parceladas em 3x ou mais no cartão! Tente outra opção!')
    else:
        juros = valor + (valor * 0.2)
        print(f'''Com um juros de 20%, suas compras ficaram por R${juros}
Parcelada em {parcelas}x de R${juros/parcelas} ''')
else:
    print('OPÇÃO NÃO ENCONTRADA! CANCELE OU TENTE NOVAMENTE!')

    