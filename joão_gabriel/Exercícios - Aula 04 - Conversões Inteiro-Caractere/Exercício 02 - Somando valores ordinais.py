"""Exercício 02"""
"""
Crie um programa que deve receber dois caracteres, somar seus valores ordinais
e printar o caractere correspondente.
"""

primeiro_caractere = input('Me forneça um caractere: ')
segundo_caractere = input('Me forneça outro caractere: ')
resultado = chr(ord(primeiro_caractere) + ord(segundo_caractere))
print(f'O resultado da soma dos valores ordinais dos caracteres '
      f'{primeiro_caractere} e {segundo_caractere} é igual a {resultado}.')
