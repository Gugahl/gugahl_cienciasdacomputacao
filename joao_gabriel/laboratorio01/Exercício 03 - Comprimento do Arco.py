"""
Laboratorio 01 - Exercício 03
    Arco da Circunferência
"""

lab = 'Laboratório 01'
frase = 'Área do Trapézio'
print('-=-' * 20)
print(f'{lab:^60}')
print(f'{frase:^60}')
print('-=-' * 20)

pi = 3.14
angulo_30_graus = 30
angulo_45_graus = 45
angulo_60_graus = 60
raio_1 = 5
raio_2 = 6
raio_3 = 8
comprimento_do_arco_1 = (pi/180)*angulo_30_graus*raio_1
comprimento_do_arco_2 = (pi/180)*angulo_45_graus*raio_2
comprimento_do_arco_3 = (pi/180)*angulo_60_graus*raio_3

print(f'O comprimento do arco da circunferência 01 é: {comprimento_do_arco_1:.2f};\n'
      f'O comprimento do arco da circunferência 02 é: {comprimento_do_arco_2:.2f};\n'
      f'O comprimento do arco da circunferência 03 é: {comprimento_do_arco_3:.2f}.')
