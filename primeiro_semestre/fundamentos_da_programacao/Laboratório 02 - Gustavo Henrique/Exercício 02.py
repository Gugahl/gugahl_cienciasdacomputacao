"""
    Laboratório 02
     Exercício 02
"""
from math import sqrt as r
from math import pow as p

lab = 'Laboratório 02'
frase = 'Distância entre dois pontos'
print('-=' * 30, '\n' + f'{lab:^60}' '\n' + f'{frase:^60}' '\n' + '-=' * 30)

calcular_distancia_1 = r(p((3 - 1), 2) + p((4 - 1), 2))
calcular_distancia_2 = r(p((10 - 0), 2) + p((10 - 0), 2))
calcular_distancia_3 = r(p((20 - 2), 2) + p((30 - 7), 2))

print(f"A distância entre os pontos (1, 1) e (3, 4) é: {calcular_distancia_1:.2f}")
print(f"A distância entre os pontos (0, 0) e (10, 10) é: {calcular_distancia_2:.2f}")
print(f"A distância entre os pontos (2, 7) e (20, 30) é: {calcular_distancia_3:.2f}")
