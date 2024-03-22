"""Exercício 01"""
"""
Crie um programa que deve receber do usuário um número de 4 dígitos.
Converta o número resultante dos 2 primeiros e dos 2 últimos dígitos deste
número em caracteres e printe-os concatenados.
Ex: Entrada: 6798 Saída: Cb
"""

import math as m
num = int(input("Digite um numero inteiro de 4 caracteres: "))
num = str(num)
primeiro_caractere = chr(int(num[:2]))
segundo_caractere = chr(int(num[2:]))
print(primeiro_caractere + segundo_caractere)
