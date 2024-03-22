"""
    Laboratório 02
     Exercício 02
"""
from math import sqrt as r
from math import pow as p

lab = 'Laboratório 02'
frase = 'Distância entre dois pontos'
print('-=' * 30, '\n' + f'{lab:^60}' '\n' + f'{frase:^60}' '\n' + '-=' * 30)

def calcular_distancia(x1, y1, x2, y2):
    return r(p((x2 - x1), 2) + p((y2 - y1), 2))

print(f"A distância entre os pontos (1, 1) e (3, 4) é: {calcular_distancia(1, 1, 3, 4):.2f}")
print(f"A distância entre os pontos (0, 0) e (10, 10) é: {calcular_distancia(0, 0, 10, 10):.2f}")
print(f"A distância entre os pontos (2, 7) e (20, 30) é: {calcular_distancia(2, 7, 20, 30):.2f}")
