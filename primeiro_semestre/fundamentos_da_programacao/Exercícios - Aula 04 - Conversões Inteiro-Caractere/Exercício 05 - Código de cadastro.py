"""Exercício 05"""
from random import randint
"""
● Crie um programa que deve preencher uma ficha de inscrição do usuário, coletando
algumas informações do mesmo e gerando um código de cadastro. Ao fim o cadastro
completo deve ser printado de forma organizada.
○ Informações que devem ser coletadas:
■ Nome
■ Idade (10 ≤ idade ≤ 99)
■ Peso (10 ≤ peso ≤ 99)
○ O código de cadastro deve ser gerado concatenando cada um dos elementos abaixo:
■ As duas primeiras letras do nome
■ A idade invertida
■ O peso concatenado de um número aleatório entre 0 e 9, concatenado do peso invertido
"""

nome = input('Qual é o seu nome? ')
idade = int(input('Quantos anos você tem?(10, 99) '))
peso = int(input('Quantos quilos você tem?(10, 99) '))
idade = str(idade)
peso = str(peso)
numero_aleatorio = str(randint(0, 9))
codigo = nome[0:2] + idade[1] + idade[0] + peso + numero_aleatorio + peso[1] + peso[0]
print(f"O código gerado foi: {codigo}")
