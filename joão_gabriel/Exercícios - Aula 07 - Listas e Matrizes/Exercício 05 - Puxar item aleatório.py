"""Exercício #05 - Puxar item aleatório"""
from random import choice
"""
Escreva um programa que selecione um item aleatoriamente de uma lista.
"""

exercicio = 'Exercício #05'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

lista = ['Ian Neves', 'Gustavo Gaiofato', 'Bebel Abelhinha', 'Luide']
print(choice(lista))
