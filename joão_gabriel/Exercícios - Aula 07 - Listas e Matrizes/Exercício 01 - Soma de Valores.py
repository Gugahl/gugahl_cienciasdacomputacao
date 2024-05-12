"""Exercício #01 - Soma de Valores"""
"""
Faça um programa que some todos os itens em uma lista.
"""

lista = [10, 20, 30, 40, 50, 60]
soma = 0

exercicio = 'Exercício #01'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

for num in lista:
    soma += num
print(f'\nO resultado da soma de todos os itens da lista:\n'
      f'[10, 20, 30, 40, 50, 60] foi {soma}.')
