# Alinhamento

# esquerda
text = "Oi"
print(f"{text:<10}")  # Resultado: "Oi        "

# direita
text = "Oi"
print(f"{text:>10}")  # Resultado: "        Oi"

# centro
text = "Oi"
print(f"{text:^10}")  # Resultado: "    Oi    "

minha_string = "O curso foi iniciado em Dezembro e durou cinco meses."
print(minha_string.ljust(100, "-")) # adiciona "-" à esquerda
# -----------------------------------------------O curso foi iniciado em Dezembro e durou cinco meses.

minha_string = "O curso foi iniciado em Dezembro e durou cinco meses."
print(minha_string.rjust(100, "-")) # adiciona "-" à direita
#O curso foi iniciado em Dezembro e durou cinco meses.-----------------------------------------------

minha_string = "O curso foi iniciado em Dezembro e durou cinco meses."
print(minha_string.center(100, "-")) # adiciona "-" à esquerda e à direita
#-----------------------O curso foi iniciado em Dezembro e durou cinco meses.------------------------

# colocar duas variavéis em intervalos diferentes no mesmo for
# Intervalo da primeira variável (x) de 0 a 5
# Intervalo da segunda variável (y) de 10 a 15
for x, y in zip(range(0, 6), range(10, 16)):
    print(f"x: {x}, y: {y}")
# Resultado:
# x: 0, y: 10
# x: 1, y: 11
# x: 2, y: 12
# x: 3, y: 13
# x: 4, y: 14
# x: 5, y: 15
