"""Exercício 4A"""
from random import randint
""" 
Crie um programa para um jogo de adivinhação, onde o jogo só para quando o jogador
der a entrada -1. O jogador deve escolher entre os números de 1 a 7 e o programa deve
dizer se ele acertou ou não o número que foi sorteado. Um número novo deve ser sorteado
a cada iteração do programa! Faça com que a saída seja formatada da mesma maneira do exemplo
abaixo. Lembre-se de usar a biblioteca random e sua função randint para gerar os números.
Exemplo: Entrada: 4     Saída: Errou! O número era 2.
                  3            Acertou!
                  7            Errou! O número era 4
                 -1            Jogo finalizado.
"""
user = 0
while user != -1:  # while True:
    pc = randint(1, 7)
    user = int(input(" "))
    if user == -1:
        break
    elif user == pc:
        print("Acertou!")
    else:
        print(f"Errou! O número era {pc}.")
print("Jogo finalizado.")
