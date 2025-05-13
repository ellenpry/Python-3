# Dicionário em python

dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados['nome']}: '))
if dados['média'] >= 7:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'

for k, v in dados.items():
    print(f'{k.title()} é igual a {v}!')