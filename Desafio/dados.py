# 
import moedas

def leiadinheiro(valor):
    valido = False
    while not valido:  # enquanto valido não for True
        entrada = str(input(valor)).replace(',', '.').strip()  # recebe um novo valor, substitui a virgula por ponto e limpa os espaços
        
        if entrada.isalpha() or entrada == "":  # se for letra ou espaço vazio, mostra a mensagem de erro e returno o input por causa do while
            print(f'ERRO! "{entrada}" não é um preço válido!')
        else: # se nao, ele é validado e sai do loop while
            valido = True
            
    return float(entrada) # retorna como float


