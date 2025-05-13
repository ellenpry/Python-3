# Analisando e gerando 

def notas(*num, sit = False):
    """Análisa notas e situações de vários alunos.

    Args:
        num (aceita todos os tipos de dados): _recebe uma ou mais notas dos alunos_.
        sit (bool, optional): _indica se deve ou não mostrar a situação dos alunos_. Defaults to False.

    Returns:
        dic (dict): _dicionário com o 'Total' de notas, 'Maior' nota, 'Menor' nota, 'Média' das notas e a 'Situação' Ruim/Razoável/Boa (opcional)_
    """
    dic = {}
    total = 0
    dic['Total'] = len(num)
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    for nota in num:
        total += nota
    dic['Média'] = total/len(num)  # ou sum(num)/len(num)
    if sit is True:
        if dic['Média'] < 6:
            dic['Situação'] = 'Ruim'
        elif dic['Média'] >= 6 and dic['Média'] <= 7:
            dic['Situação'] = 'Razoável'
        else: 
            dic['Situação'] = 'Boa'
    return dic

res = notas(9, 4, 6, 10, sit = True)
help(notas)