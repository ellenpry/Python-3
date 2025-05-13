# Contando Vogais em Tupla

palavras = ('python', 'desenvolvedor', 'web', 'aprender', 'programar', 'leitura', 'livros', 'bibliotaca', 'trabalhar', 'futuro')

vogais = ('a', 'e', 'i', 'o', 'u')
lista = []
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais →', end = ' ')
    for l in p:
        if l in vogais:
            print(l, end = ' ')