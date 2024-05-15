"""
     Laboratorio 01 - Exercício 04
      Distância entre dois pontos
"""

lab = 'Laboratório 01'
frase = 'Distância entre dois pontos'
print('-=' * 30, '\n' + f'{lab:^60}' '\n' + f'{frase:^60}' '\n' + '-=' * 30)

distancia_1 = (((3 - 1) ** 2) + ((4 - 1) ** 2)) ** 0.5
distancia_2 = (((10 - 0) ** 2) + ((10 - 0) ** 2)) ** 0.5
distancia_3 = (((20 - 2) ** 2) + ((30 - 7) ** 2)) ** 0.5

print(f'A distância entre os dois pontos (1, 1) e (3, 4) em um plano cartesiano é: {distancia_1:.2f};\n'
      f'A distância entre os dois pontos (0, 0) e (10, 10) em um plano cartesiano é: {distancia_2:.2f};\n'
      f'A distância entre os dois pontos (2, 7) e (20, 30) em um plano cartesiano é: {distancia_3:.2f}.')
