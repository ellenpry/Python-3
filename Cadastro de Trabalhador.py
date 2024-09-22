# Cadastro de Trabalhador

dados = {}
from datetime import date

dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
dados['idade'] = anoatual - ano
dados['ctps'] = int(input('Carteira de Trabalho [0 para NÂO TENHO]: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    anoapos = dados['contratação'] + 35
    dados['aposentadoria'] = anoapos - ano
print()
print(dados)
print()
for k, v in dados.items():
    print(f'{k.title()} tem o valor {v}')
print()
    
