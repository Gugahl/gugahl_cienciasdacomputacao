"""Exercício 04 - Tabuada v2.0 e v3.0"""
from time import sleep
"""
Escreva um programa que mostre a tabuada de um número informado pelo usuário,
conforme mostrado:
(Faça sua versão com while e com for)
"""
"""
num = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 6)
for c in range(1, 11):
    print(f'{num} x {c:2} = {(c*num):2}')
    sleep(1)
print('-=' * 6)
"""
"""
num = int(input('Digite um número para ver sua tabuada: '))
c = 1
print('-=' * 6)
while c != 11:
    print(f'{num} x {c:2} = {(c*num):2}')
    c += 1
    sleep(1)
print('-=' * 6)
"""
