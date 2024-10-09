# Função para fatorial

def fatorial(n, show = False):
    """ Calcula o fatorial de um número.

    Args:
        n (int): O número a ser calculado.
        show (bool, optional): Mostra ou não a conta. Defaults to False.
    """
    print(f'Fatorial do número {n}:', end = ' ')
    fact = 1
    if show is True:
        for c in range(n, 1, -1):
            fact *= c
            print(f'{c} x', end = ' ')
        print(f'1 = {fact}')    
    else:
        for c in range(n, 0, -1):
            fact *= c
        print(fact)
            
num = int(input('Digite um número: '))
res = str(input('Deseja mostrar o número sendo fatorado? [S/N] ')).upper().strip()
if res[0] == 'S':
    fatorial(num, show = True)
else:
    fatorial(num)
    
help(fatorial)