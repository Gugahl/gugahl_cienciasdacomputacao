"""Exercício #06 - Dimensões de uma matriz"""
"""
Escreva um programa que diga as dimensões de uma matriz (pré-estabelecida).
Ex: [[1, 2, 3], [1, 2, 3]]
(2, 3)
"""

exercicio = 'Exercício #06'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

lista = [[3, 2, 1], [1, 2, 3]]
sublista = lista[0]
print(f'({len(lista)}, {len(sublista)})')
