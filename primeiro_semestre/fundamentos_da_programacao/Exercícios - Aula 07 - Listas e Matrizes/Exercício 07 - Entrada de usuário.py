"""Exercício 07 - Entrada de usuário"""
"""
Escreva um programa que deve receber uma matriz do usuário e printar ao fim a soma de
cada coluna da matriz recebida. O usuário primeiro deve entrar com as dimensões (linhas
e colunas da matriz) e então alimentar os números de cada linha.
"""

exercicio = 'Exercício #07'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []
for l in range(linhas):
    linha = []
    for c in range(colunas):
        linha.append(0)
    matriz.append(linha)

print(f'\nMatriz criada:')
print(matriz, f'\n')

soma_colunas = [0] * colunas
for l in range(linhas):
    for c in range(colunas):
        matriz[l][c] = int(input(f"Digite um valor para [{l + 1}, {c + 1}]: "))
        soma_colunas[c] += matriz[l][c]

print(f'\nMatriz alimentada:')
print(matriz)

print("\nSoma de cada coluna:")
for soma in soma_colunas:
    print(soma)
