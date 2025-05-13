# Um print especial

def escreva(msg):
    tam = len(msg) + 2
    print('-' * tam)
    print(msg.center(tam))
    print('-' * tam)

for m in range(1, 4):
    msg = str(input(f'Escreva a {m}° mensagem: '))
    escreva(msg)