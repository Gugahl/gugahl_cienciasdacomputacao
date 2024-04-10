"""
    Laboratório 02
     Exercício 01B
"""
from math import pi as p 
from math import radians as r 

conversao_formula_30 = (30/180) * p 
conversao_formula_60 = (60/180) * p 
conversao_formula_90 = (90/180) * p 
conversao_formula_180 = (180/180) * p 

conversao_radians_30 = r(30)
conversao_radians_60 = r(60)
conversao_radians_90 = r(90)
conversao_radians_180 = r(180)

grauspararadianos = 'Graus para radianos'
print('-=' * 30, '\n' + f'{grauspararadianos:^60}', '\n' + '-=' * 30)
print(f'Com a fórmula:\n'
    f' O valor em radianos de 30° é {conversao_formula_30:.2f};\n', 
    f'O valor em radianos de 60° é {conversao_formula_60:.2f};\n',
    f'O valor em radianos de 90° é {conversao_formula_90:.2f};\n',
    f'O valor em radianos de 180° é {conversao_formula_180:.2f}.\n')

print(f'Importando a biblioteca math:\n'
    f' O valor em radianos de 30° é {conversao_radians_30:.2f};\n', 
    f'O valor em radianos de 60° é {conversao_radians_60:.2f};\n',
    f'O valor em radianos de 90° é {conversao_radians_90:.2f};\n',
    f'O valor em radianos de 180° é {conversao_radians_180:.2f}.')
