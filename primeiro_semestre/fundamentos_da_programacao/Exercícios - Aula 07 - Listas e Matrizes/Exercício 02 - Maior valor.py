"""Exercício #02 - Maior valor"""
"""
Faça um programa para pegar o maior número em uma lista.
"""

lista = [10, 20, 70, 40, 30, 60]
maior = 0

exercicio = 'Exercício #02'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

for num in lista:
    posi = len(lista)
    if posi == 0:
        maior = num
    elif num > maior:
        maior = num
print(f'O maior valor da lista foi {maior}.')
