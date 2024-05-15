"""Exercício #04 - Encontrar Strings"""
"""
Escreva um programa que receba uma palavra e retorne em que índice da lista
(pré-estabelecida) de palavras a que foi recebida está, ou se não estiver contida na lista,
printe uma mensagem de erro.
"""

exercicio = 'Exercício #04'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

stringrecebida = input("Digite uma string: ")
lista = ['Bolsonaro', 'Lula', 'Ciro']

if stringrecebida in lista:
    print(f"A string recebida está no índice: ", lista.index(stringrecebida))
else:
    print(f"A string recebida não está dentro da lista.")
