"""
    Laboratório 02
     Exercício 05
"""
from random import randrange as rr

lab = 'Laboratório 02'
frase = 'Múltiplos de 5'
print('-=' * 30, '\n' + f'{lab:^60}' '\n' + f'{frase:^60}' '\n' + '-=' * 30)

multiplosde5 = rr(0, 100, 5)
print(f'O número gerado foi: {multiplosde5}.')
