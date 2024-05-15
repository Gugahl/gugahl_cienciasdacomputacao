"""
    Laboratório 02
     Exercício 03
"""
from random import random as r
from math import ceil as t
from math import floor as c

lab = 'Laboratório 02'
frase = 'Manipulando números pseudoaleatórios'
print('-=' * 30, '\n' + f'{lab:^60}' '\n' + f'{frase:^60}' '\n' + '-=' * 30)

numero = r()
print(f"A pseudoaleatoriedade da função random gerou o número {numero}.")
print(f"O número {numero:.2f} arredondado para cima é igual a: {t(numero)}.")
print(f"O número {numero:.2f} arredondado para baixo é igual a: {c(numero)}.")
