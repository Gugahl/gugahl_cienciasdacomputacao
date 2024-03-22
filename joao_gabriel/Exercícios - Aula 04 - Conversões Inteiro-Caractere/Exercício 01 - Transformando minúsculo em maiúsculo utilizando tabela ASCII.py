"""Exercício 01"""
"""
Crie um programa que deve receber um caractere minúsculo e printar sua versão
maiúscula.
"""

letra_minúscula = input('Digite uma letra minúscula: ')
letra_maiúscula = chr(ord(letra_minúscula) - 32)
print(f'A letra "{letra_minúscula}" em caps lock fica "{letra_maiúscula}".')
