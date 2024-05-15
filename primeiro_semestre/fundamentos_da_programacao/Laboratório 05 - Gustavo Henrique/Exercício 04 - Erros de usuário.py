"""Exercício 04 - Erros de usuário"""
from random import randint
"""
Retorne às questões 1 e 2 e altere o código fazendo com que ele evite erros
de usuário.
Q1: Evitar strings com espaço e que não contenham pelo menos 1 letra e 1
número.
Q2: Evitar entradas diferentes de números de 1 a 9.
"""

exercicio = 'Exercício 01 - Contagem de letras e números'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

frase = input('Digite algo: ')
frase = frase.replace(' ', '')
cont = len(frase) - 1
teste = numer = strin = ' '
while cont >= 0:
    teste = frase[cont].isnumeric()
    print(end='')
    if teste == True:
        numer += f'{frase[cont]}'
    else:
        strin += f'{frase[cont]}'
    cont -= 1
print(f'Letras: {strin[::-1].strip()}')
print(f'Números: {numer[::-1].strip()}')

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
