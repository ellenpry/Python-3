# Validação de Dados

sexo = str(input('Qual é o seu sexo F/M? ')).upper()
while sexo != 'F':
    print('Resposta recusada! Tente novamente!')
    sexo = str(input('Qual é o seu sexo F/M? ')).upper()
while sexo != 'M':
    print('Resposta recusada! Tente novamente!')
    sexo = str(input('Qual é o seu sexo F/M? ')).upper()
if sexo == 'F':
    print('Você se identifica com o sexo feminino! Seja bem-vinda!')
elif sexo == 'M': 
    print('Você se identifica com o sexo masculino! Seja bem-vindo!')
    
# Achei esse programa bem preconceituoso em relação a identificação de gênero!
    

