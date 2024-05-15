"""Exercício 04 - Fibonacci"""
"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... (o
próximo termo é a soma dos dois anteriores). Faça um programa capaz de
gerar a série até o n−ésimo termo, sendo este termo recebido pelo usuário.
"""

numero = int(input('Digite um número inteiro: '))
anterior = 1
penultimo = 0
print(f'{penultimo}, {anterior}', end='')
for c in range(1, numero + 1):
    fibonacci = penultimo + anterior
    print(f', {fibonacci}', end='')
    penultimo = anterior
    anterior = fibonacci
