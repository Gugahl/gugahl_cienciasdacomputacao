"""Exercício 01 - Contagem ao cubo"""
"""
Faça um programa que apresente o cubo de todos os números de 1 até um
número recebido.
"""

num = int(input("Digite um número inteiro: "))
cont = 1
while cont != num + 1:
    print(f'{cont}³ =', cont*cont*cont)
    cont += 1 
