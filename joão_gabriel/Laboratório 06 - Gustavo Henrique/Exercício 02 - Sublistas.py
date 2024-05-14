"""Exercício 02 - Sublistas"""
"""
Crie um programa que deve quebrar uma lista em várias sublistas a cada
enésimo valor. O valor de N deve ser recebido pelo usuário, a lista original
pode ser pré-estabelecida e deve contar ao menos 10 valores.
Exemplo:
Entrada: N = 3, Lista original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Saída: Sublistas: [1, 2, 3], [4, 5, 6], [7, 8, 9], [10]
"""

exercicio = 'Exercício #02'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input("Digite o valor de N: "))

sublistas = []


for i in range(0, len(lista_original), n):
    sublista = lista_original[i:i+n]
    sublistas.append(sublista)

print("Sublistas:", sublistas)
