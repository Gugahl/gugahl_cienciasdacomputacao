"""Exercício 04"""
from math import floor
"""
Crie um programa que deve gerar o nome de um possível filho(a) de um
casal. Você deverá receber o primeiro nome de cada um dos pais e então
deverá pegar a primeira metade do nome do primeiro e concatenar a
segunda metade do nome do segundo para gerar o nome do filho(a).
○ Ex: João e Larissa = Joissa.
○ Use a função len() para descobrir o tamanho das strings e math.floor()
para arredondar tamanhos ímpares.
"""

primeira_pessoa = input('Digite o nome da primeira pessoa: ').title()
segunda_pessoa = input('Digite o nome da segunda pessoa: ').title()
filho = primeira_pessoa[:(floor(len(primeira_pessoa)/2))] + segunda_pessoa[floor(len(segunda_pessoa)/2):]
print(f'{filho}')
