"""Exercício 02 - Soma de uma série"""
"""
Faça um programa que dê o resultado da soma de uma série de n termos,
onde n é recebido pelo usuário e o formato da série é o seguinte: Para n = 5
teremos, 2 + 22 + 222 + 2222 + 22222 = 24690 (Apenas o resultado deve ser
apresentado).
"""

num = int(input("Digite um número inteiro: "))
cont = 1
soma = string = 0
while cont < num + 1:
    string = int(f'2' * cont)
    soma += string
    cont += 1
print(f'{soma}')
