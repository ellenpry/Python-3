# Validação de Dados

sexo = str(input('Infome seu sexo F/M: ')).strip().upper()[0]
while sexo not in "FM":
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo: ')).strip().upper()
if sexo == 'F':
    print('Sexo Feminino registrado com sucesso!')   
else: 
    print('Sexo Masculino registrado com sucesso!')

# Ainda não acredito que quebrei a cabeça com isso! Por que tão burra...

