# funções para moedas

def aumentar(valor = 0, sit = True, juros = 10):
    """_Calcula o aumento de um determidado preço, retornando o resultado com ou sem formatação_

    Args:
        valor (int or float, optional): _o preço que será reajustado_. Defaults to 0.
        sit (bool, optional): _define se a saída será formatada ou não_. Defaults to True.
        juros (int or float, optional): _porcentagem do aumento_. Defaults to 10.

    Returns:
        a (float): _valor reajustado, com ou sem formatação_
    """
    a = (juros/100 * valor) + valor
    return a if sit == False else moeda(a)

def diminuir(valor = 0, sit = True, desconto = 10):
    d = valor - (desconto/100 * valor)
    return d if sit == False else moeda(d)


def dobro(valor = 0, sit = True):
    v = valor * 2
    return v if sit == False else moeda(v)

def metade(valor = 0, sit = True):
    v = valor / 2
    return v if sit == False else moeda(v)

def moeda(valor = 0):
    return f'R${valor:>.2f}'.replace('.', ',')

def resumo(preco = 0, juros = True, desconto = 0):
    print('-'*33)
    print(f'{'RESUMO DO VALOR'.center(33)}')
    print('-'*33)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco)}')
    print(f'Metade do preço: \t{metade(preco)}')
    print(f'{juros}% de aumento: \t{aumentar(preco, True, juros)}')
    print(f"{desconto}% de redução: \t{diminuir(preco, True, desconto)}")