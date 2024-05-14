"""Exercício 03 - Interseção de Listas"""
"""
Crie um programa que deve ter duas listas pré-estabelecidas, uma com
inteiros e outra com strings dasquais todas são números. O programa deve
então comparar as listas e gerar uma nova lista apenas com os números que
aparecem em ambas as listas.
Exemplo:
Entrada: Lista_1: [1, 2, 3, 4, 5], Lista_2: [“1”, “7”, “2”, “8”, “4”]
Saída: [1, 2, 4]
"""

exercicio = 'Exercício #03'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ["1", "7", "2", "8", "4"]

lista_2_inteiros = [int(num) for num in lista_2]
intersecao = []
for num in lista_1:
    if num in lista_2_inteiros:
        intersecao.append(num)

print(f'Interseção: {intersecao}')