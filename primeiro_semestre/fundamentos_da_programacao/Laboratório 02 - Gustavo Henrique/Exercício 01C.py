"""
    Laboratório 02
     Exercício 01C
"""
from math import pi as p
from math import radians as r
from math import degrees as g
from math import ceil as t
#  importar manualmente da mais trabalho, mas em contrapartida consome menos do cpu
#  esse foi o maior e mais bem feito código que eu já fiz em dois meses de estudoKKKKK

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
    f'O valor em radianos de 180° é {conversao_radians_180:.2f}.\n')

retorno_formula_30 = g(conversao_formula_30)
retorno_formula_60 = g(conversao_formula_60)
retorno_formula_90 = g(conversao_formula_90)
retorno_formula_180 = g(conversao_formula_180)

retorno_radians_30 = g(conversao_radians_30)
retorno_radians_60 = g(conversao_radians_60)
retorno_radians_90 = g(conversao_radians_90)
retorno_radians_180 = g(conversao_radians_180)

radianosparagraus = 'Radianos para graus'
print('-=' * 30, '\n' + f'{radianosparagraus:^60}', '\n' + '-=' * 30)

print(f'Com a fórmula:\n'
    f' O valor em graus de {conversao_formula_30:.2f} é {t(retorno_formula_30)}°;\n', 
    f'O valor em graus de {conversao_formula_60:.2f} é {t(retorno_formula_60)}°;\n',
    f'O valor em graus de {conversao_formula_90:.2f} é {t(retorno_formula_90)}°;\n',
    f'O valor em graus de {conversao_formula_180:.2f} é {t(retorno_formula_180)}°.\n')

print(f'Importando a biblioteca math:\n'
    f' O valor em graus de {conversao_radians_30:.2f} é {t(retorno_radians_30)}°;\n', 
    f'O valor em graus de {conversao_radians_60:.2f} é {t(retorno_radians_60)}°;\n',
    f'O valor em graus de {conversao_radians_90:.2f} é {t(retorno_radians_90)}°;\n',
    f'O valor em graus de {conversao_radians_180:.2f} é {t(retorno_radians_180)}°.')
