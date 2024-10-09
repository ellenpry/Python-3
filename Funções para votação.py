# Funções para votação

def voto(anonasc):
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - anonasc
    if idade >= 18 and idade <= 70:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA.')
    elif idade >= 16 and idade <= 17 or idade > 70:
        return print(f'Com {idade} anos: VOTO FACULTATIVO.')
    
def linha():
    print('-'*35)

linha()
ano = int(input('Digite seu ano de nascimento: '))
voto(ano)
linha()