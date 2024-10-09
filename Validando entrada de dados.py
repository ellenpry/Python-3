# Validando entrada de dados

def leiaint(valor):
    valor = valor.strip()
    while not valor.isdigit():
        print('ERRO! Digite um número inteiro válido!')
        valor = input('Digite um número interio: ').strip()
    return valor
    

n = leiaint(input('Digite um número interio: '))
print(f'Você acabou de digitar o número {n}!')

