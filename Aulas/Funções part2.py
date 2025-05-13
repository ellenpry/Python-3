# docstrings

def contador(i, f, p):  # a docstring dica na primeira linha
    """
    Faz uma contagem e mostra na tela.
    Args:
        i (_int_): inicio da contagem
        f (_int_): fim da contagem
        p (_int_): passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end = '.. ')
        c += p
    print('Fim!')

help(contador)

# paramestros opcionais
def somar(a, b, c = 0):  # igualo o parametro à 0
    s = a + b + c
    print(f'A soma é igual a {s}')
    print()

somar(1, 2) # posso colocar apenas 2 parametros porque o c é opcional

# Escopos
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')  # o N é um escopo global, porque ela foi definida fora da função
    print(f'na função teste, x vale {x}')  # o X é um escopo local, pois ela foi definida dentro da função
    print()
# programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()

# mais sobre escopos
def test(b):
    global a  # chamei o A global, pos isso o A global deixa de valer 5 e começa a veler 8
    a = 8   # A é um escopo local
    b += 4  # B é um escopo local
    c = 2   # C é um escopo local
    print(f'''"a" dentro vale {a}
"b" dentro vale {b}
"c" dentro vale {c}
          ''')
    
# programa principal
a = 5   # é um escopo global
print(f'"a" fora vale {a}')
test(a)

# returne
def soma(a = 0, b = 0, c = 0): # sao parametros opcionais
    s = a + b + c
    return s # o S retorna á alguma variavel, por isso é preciso declarar. no caso pra variavel "resultado"

resultado = soma(2, 4, 5) # o S retorna pra cá
print(f'A soma é igual a {resultado}')

r1 = soma(1, 2, 3)
r2 = soma(3, 4)
r3 = soma(5)
print(f'os resultados são {r1}, {r2} e {r3}')  # posso colocar todos os resultados juntos desse jeito