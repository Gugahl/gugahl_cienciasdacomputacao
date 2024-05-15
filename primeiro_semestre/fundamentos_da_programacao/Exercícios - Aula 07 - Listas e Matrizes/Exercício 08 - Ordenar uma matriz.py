"""Exercício 08 - Ordenar uma matriz"""
"""
Escreva um programa que deve ordenar uma matriz (pré-estabelecida) na ordem
ascendente de acordo com as somas de suas linhas.
Ex: [[1, 2, 3], [2, 4, 5], [1, 1, 1]] → [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""
# incompleto
exercicio = 'Exercício #08'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

matriz = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

print(matriz)

matriznova = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = menor = meio = 0
soma = [0, 0, 0]
for l in range(0, 3):
    for c in range(0, 3):
        soma[l] += matriz[l][c]
        if soma[l] == 0:
            menor = soma[l]
            meio = soma[l]
            maior = soma[l]
        elif soma[l] > maior:
            maior = soma[l]
        elif soma[l] < menor:
            menor = soma[l]
        else:
            meio = soma[l]
    print(f'Soma {l + 1}: ', soma[l], sep='', end=', ' if l < 2 else '.')
print(f'Maior: {maior}, Menor: {menor}, Meio: {meio}')

for l in range(0, 3):
    if l == 0:
        for l in range(0, 1):
            for c in range(0, 3):
                if c == 0:
                    matriznova[l][c] = matriz[l][c]
                elif c == 1:
                    matriznova[l][c] = matriz[l][c]
                else:
                    matriznova[l][c] = matriz[l][c]    
    elif l == 1:
        for l in range(1, 2):
            for c in range(0, 3):
                if c == 0:
                    matriznova[l][c] = matriz[l][c]
                elif c == 1:
                    matriznova[l][c] = matriz[l][c]
                else:
                    matriznova[l][c] = matriz[l][c]
    elif l == 2:
        for l in range(2, 3):
            for c in range(0, 3):
                if c == 0:
                    matriznova[l][c] = matriz[l][c]
                elif c == 1:
                    matriznova[l][c] = matriz[l][c]
                else:
                    matriznova[l][c] = matriz[l][c]

print(f'\n', matriznova, sep='')
