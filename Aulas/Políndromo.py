# Políndromo

 # Cores no Terminal
cor = {'clean': '\033[m', 
       'gray': '\033[30m', 
       'red': '\033[31m', 
       'green': '\033[32m', 
       'yellow': '\033[33m',
       'purple': '\033[34m',
       'pink': '\033[35m', 
       'blue': '\033[36m'}

sentence = str(input('Escreva uma frase: ')).strip().upper() #tirei os espaços e coloquei em maiusculo
words = sentence.split() #separei por palavras
junto = ''.join(words) #juntei as palavras
inverse = ''
for letra in range(len(junto) -1, -1, -1): #contei a quant. de letras com o len() ((com o -1 pois a contagem começa do 0)); o segundo -1 é pra indicar que começa na primeira letra; o terceiro -1 serve pra indicar que vai ser de trás pra frente.]
    inverse += junto[letra] #consigo acessar o caractere da string 'junto' no indice 'letra'
# sem a necessidade do loop, eu consigo inverter uma string desse modo: INVERSE = JUNTO[::-1] 
if inverse == junto:
    print(f'A frase "{sentence}" é um políndromo!')
    print(cor['green'], junto,'=', inverse, cor['clean'])
else:
    print(f'A frase "{sentence}" NÃO é um políndromo!')
