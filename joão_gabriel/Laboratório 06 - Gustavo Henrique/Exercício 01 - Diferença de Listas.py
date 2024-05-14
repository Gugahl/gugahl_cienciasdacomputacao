"""Exercício 01 - Diferença de Listas"""
"""
Crie um programa que deve printar a diferença entre duas listas já
pré-estabelecidas. É obrigatório o uso de um loop para fazer a comparação
entre as listas.

Exemplo:
Listas: [1, 2, 3, 4] e [2, 4]
Saída: Diferença [1, 3].
"""

exercicio = 'Exercício #01'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

lista1 = [1, 2, 3, 4]
lista2 = [2, 4]
diferenca = []

for num in lista1:
    if num not in lista2:
        diferenca.append(num)

print(f'Diferença {diferenca}')
