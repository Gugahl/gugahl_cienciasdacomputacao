"""Exercício 04 - Lista Ordenada do Usuário"""
"""
Crie um programa que deve receber 6 números e depois gerar uma lista em
ordem crescente destes números.

Exemplo:
Entrada: 5
10
2
8
1
2
Saída: Lista ordenada: [1, 2, 2, 5, 8, 10]
"""

exercicio = 'Exercício #04'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

numeros = []
for i in range(6):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)
numeros_ordenados = sorted(numeros)

print(f"Lista ordenada: {numeros_ordenados}")
