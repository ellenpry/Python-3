# Tratamento de erros e excessões

# exemplo 1
try: # ele tenta rodar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except: # caso der um problema mostra a mensagem
    print('Infelizmente tivemos um problema.')
    
else: # caso der certo
    print(f'O resultado é {r}')
    
finally: # acontece independente se ser erro ou não
    print('Volte sempre! Muito obrigado!')



# exemplo 2
try:
    n = int(input('Digite um número: '))
except Exception as erro: # a classe Exception como erro (uma variavel)
    print(f'O problema encontrado foi: {erro.__class__}') # consigo mostrar a classe do erro e outras coisas tambem (cause, context...)
else:
    print(f'Você digitou o número {n}')
    
    
    
# exemplo 3
try:
    n1 = int(input('1° número: '))
    n2 = int(input('2° número: '))
    t = n1 / n2
except (ValueError, TypeError):  # se der problema de ValueError ou de TypeError, faço algo especifico
    print('Tivemos um problema com os tipos de dados que você digitou.')
    
except ZeroDivisionError: # caso tente dividir por zero, mostre uma mensagem diferente
    print('Não é possível dividir um número por zero.')
    
except KeyboardInterrupt: # caso não escreva nada
    print('O usuário preferiu não informar os dados.')

else:
    print(f'{n1}/{n2} = {t:.1f}')

    