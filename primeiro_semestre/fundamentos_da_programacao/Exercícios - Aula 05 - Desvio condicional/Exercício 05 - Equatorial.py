"""Exercício 05 - Equatorial"""
"""
Escreva um programa que calcule o preço
a pagar pela energia elétrica. Pergunte a
quantidade Kwh consumida e o tipo de
instalação: R para residências, I para
indústria e C para comércios. Calcule o
preço a pagar de acordo com a tabela a
seguir
"""

consumo = float(input('Quantos kw/h foram utilizados? '))
tipo = str(input("Qual foi o tipo de instalação (R para Residências/I para Indústria/C para comércios)? ")).upper().strip()[0]

while tipo not in "RIC":
    tipo = str(input("Qual foi o tipo de instalação (R para Residências/I para Indústria/C para comércios)? "))
    if tipo in 'RIC':
        break
if tipo == 'R':
    if consumo <= 500:
        valor = consumo * 0.4
    elif consumo > 500:
        valor = consumo * 0.65
elif tipo == 'I':
    if consumo <= 1000:
        valor = consumo * 0.55
    elif consumo > 1000:
        valor = consumo * 0.6
elif tipo == 'C':
    if consumo <= 5000:
        valor = consumo * 0.55
    elif consumo > 5000:
        valor = consumo * 0.6
print(f'Valor atualizado de R${valor} para o mês de abril de 2024.')
