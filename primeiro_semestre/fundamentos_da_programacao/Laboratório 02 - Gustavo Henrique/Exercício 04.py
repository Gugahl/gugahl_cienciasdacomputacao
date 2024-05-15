"""
    Laboratório 02
     Exercício 04
"""
from math import factorial as f
from random import randint as r

lab = 'Laboratório 02'
frase = 'Fatorial de um número aleatório'
print('-=' * 30, '\n' + f'{lab:^60}' '\n' + f'{frase:^60}' '\n' + '-=' * 30)

numero = r(1, 100)
print(f'O número foi: {numero};')
print(f'O resultado do seu fatorial foi: {f(numero)}.')
