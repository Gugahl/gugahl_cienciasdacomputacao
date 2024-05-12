"""Exercício 4B"""
"""
Crie um programa que deve receber números inteiros e dizer se eles são ímpar ou par, até
que o usuário entre com 0.
"""

user = 1
while user != 0:  # while True
    user = int(input(" "))
    if user == 0:
        break
    if user % 2 == 1:
        print("Ímpar")
    else:
        print("Par")
print("Finalizado!")
