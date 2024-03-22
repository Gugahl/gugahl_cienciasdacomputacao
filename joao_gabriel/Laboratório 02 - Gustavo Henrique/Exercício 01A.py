"""
    Laboratório 02
     Exercício 01A
"""
from math import pi as p

conversao_30 = (30/180) * p
conversao_60 = (60/180) * p
conversao_90 = (90/180) * p
conversao_180 = (180/180) * p

grauspararadianos = 'Graus para radianos'
print('-=' * 30 + '\n' +  f'{grauspararadianos:^60}' + '\n' + '-=' * 30)
print(f' O valor em radianos de 30° é {conversao_30:.2f};\n', 
    f'O valor em radianos de 60° é {conversao_60:.2f};\n',
    f'O valor em radianos de 90° é {conversao_90:.2f};\n',
    f'O valor em radianos de 180° é {conversao_180:.2f}.')
