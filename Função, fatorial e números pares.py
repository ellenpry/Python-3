# Função e fatorial

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial do número {n} é {fatorial(n)}')  # printando o fatorial de um número

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}') # juntando varios fatoriais no mesmo print

def par(n = 0): # retornando True ou False
    if n % 2 == 0:
        return True
    else:
        return False
    
res = par(n)
if res is True:
    print(f'o número {n} é par!')
else:
    print(f'O número {n} é ímpar!')