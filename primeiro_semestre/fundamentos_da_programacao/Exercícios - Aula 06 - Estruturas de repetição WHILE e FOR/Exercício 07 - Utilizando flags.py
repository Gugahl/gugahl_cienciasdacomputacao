"""Exercício 07 - Utilizando flags"""
"""
Escreva um programa que deve receber inteiros do usuários até que o usuário digite o número
-1. No fim, ele o programa deve mostrar a soma dos inteiros recebidos e sua média.
"""

cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == -1:
        break
    cont += 1
    soma += num

print(f'Foram informados: {cont} números;\n'
      f'A soma desses valores foi: {soma};\n'
      f'A média desses valores foi: {soma/cont}.')
