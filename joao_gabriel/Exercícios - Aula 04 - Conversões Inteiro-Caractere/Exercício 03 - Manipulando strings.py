"""Exercício 03"""
"""
Crie um programa que deve receber do usuário 2 palavras e 1 inteiro.
Depois, o programa deve fazer 3 prints:
○ O primeiro deve mostrar as palavras concatenadas.
○ O segundo deve printar uma palavra em cada linha no mesmo print.
○ O terceiro deve repetir as duas palavras o número de vezes que foi
recebido pelo inteiro que o usuário informou.
"""

primeira_palavra = input('Digite uma palavra: ')
segunda_palavra = input('Digite outra palavra: ')
numero = int(input('Digite um número inteiro: '))
print(f'\nPrimeiro:\n' f'{primeira_palavra+segunda_palavra};')
print(f'\nSegundo:\n' f'{primeira_palavra}\n' f'{segunda_palavra};')
print(f'\nTerceiro:\n' f'{primeira_palavra*numero}\n'
      f'{segunda_palavra*numero}\n' f'{(primeira_palavra+segunda_palavra)*numero}')
