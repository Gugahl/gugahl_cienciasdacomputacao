"""Exercício 02 - Jogo da advinhação"""
from random import randint
"""
Crie um programa que deve rodar um jogo de adivinhação de número. O
programa deve selecionar aleatoriamente um número de 1 a 9 e então pedir
para o usuário adivinhar o número selecionado (sem informá-lo, obviamente).
O usuário deve então entrar com um número de 1 a 9 e o programa deve
responder se ele acertou ou não o número, apresentando o número que foi
sorteado.
Entrada: 7 Saída: Você errou! O número correto era 4! :(
"""

exercicio = 'Exercício 02 - Jogo de Advinhação'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30)
conttotal = contven = 0
while True:
    computador = randint(1, 9)  # Li a doc e o ponto final do randint é inclusivo
    usuario = int(input("\nDigite um número inteiro de (1 a 9): "))
    while usuario < 1 or usuario > 9:
        usuario = int(input("ERRO! Digite um número inteiro de (1 a 9): "))
    conttotal += 1
    if usuario != computador:
        print(f"Você errou! O número correto era {computador}! :(")
    else:
        print("Você acertou! Parabéns! :)")
        contven += 1
    continuar = input("Deseja continuar? (S/N): ").upper().strip()[0]
    while continuar not in 'SN':
        continuar = input("Deseja continuar? (S/N): ").upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
print(f"Programa encerrado!\n"
      f"Você jogou {conttotal} partidas;\n"
      f"Você venceu {contven} partidas.")
