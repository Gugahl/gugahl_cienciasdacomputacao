"""Exercício 03 - Fatorial"""
"""
Faça um programa que calcule o fatorial de um número recebido.
"""

numero = int(input("Digite um número inteiro: "))
contador = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(f' x ' if contador > 1 else f' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
