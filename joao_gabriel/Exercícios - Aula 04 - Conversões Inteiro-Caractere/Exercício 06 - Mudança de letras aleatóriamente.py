"""Exercício 06"""
from random import randint as ri
"""
● Crie um programa que deve receber uma palavra (com no mínimo 5 caracteres)
e depois deve gerar uma nova palavra seguindo as regras abaixo:
○ A primeira e a última letra da palavra devem ser trocadas por outras letras
escolhidas aleatoriamente da própria palavra.
○ Ex:
■ Entrada: Padaria
■ Saída: dadariP
■ Obs: As letras não devem trocar de lugar, apenas deve ser selecionada uma
outra letra da palavra e substituir a primeira/última por ela.
"""

palavra = input("Digite uma palavra de no minimo 5 letras: ")
qtd = len(palavra)
letra1 = palavra[ri(0, qtd)]
entre_letras = palavra[1:qtd - 1]
letra2 = palavra[ri(0, qtd)]
nova_palavra = letra1 + entre_letras + letra2
print(nova_palavra)
