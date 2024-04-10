"""Exercício 02 - Comparador de números"""
"""
Escreva um programa que receba 3 números e mostre o maior deles.
"""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))

if n1 >= n2 and n1 >= n3:
    print(f'O maior foi {n1}.')
elif n2 >= n1 and n2 >= n3:
    print(f'O maior foi {n2}.')
elif n3 >= n1 and n3 >= n2:
    print(f'O maior foi {n2}.')
