"""Exercício 05 - Média aritmética"""
"""
Escreva um programa que calcule a média aritmética dos N números informados pelo
usuário (com precisão de 2 casas decimais), o valor de N também deve ser recebido
do usuário.
(Faça sua versão com while e com for)
"""
"""
num = int(input("Digite o número de valores a ser recebido: "))
soma = 0
for c in range(1, num + 1):
    n = float(input(f"Digite o {c}º número: "))
    soma += n
print(f'A média entre os {num} valores recebidos foi {(soma/num):.2f}.')
"""
"""
num = int(input("Digite o número de valores a ser recebido: "))
soma = cont = 0
while cont != num:
    cont += 1
    n = float(input(f"Digite o {cont}º número: "))
    soma += n
print(f'A média entre os {num} valores recebidos foi {(soma/num):.2f}.')
"""
