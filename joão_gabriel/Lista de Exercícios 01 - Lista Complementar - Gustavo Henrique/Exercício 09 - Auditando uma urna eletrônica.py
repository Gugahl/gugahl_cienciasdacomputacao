"""Exercício 09 - Auditando uma urna eletrônica"""
import pygame
from time import sleep
"""
Louvado seja o pneu
Em uma eleição presidencial existem quatro candidatos. Os votos são
informados por meio de código. Os códigos utilizados são:
1, 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela
ex: 1 - Jose/ 2 - João/ etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
● O total de votos para cada candidato;
● O total de votos nulos;
● O total de votos em branco;
● A percentagem de votos nulos sobre o total de votos;
● A percentagem de votos em branco sobre o total de votos.
Cada linha de entrada do usuário deve ser composta apenas de um número
de 1 a 6, para uma das opções. O programa para ao receber a entrada 0, e
então disponibiliza os resultados.
Dica: Criar uma variável contadora para cada uma das 6 opções (4 para os
candidatos e 1 para nulo e outra para branco).
"""

eleicoes = 'Eleições 2022'
print(f'=-' * 20 + f'\n' + f'{eleicoes:^40}' + f'\n' + f'=-' * 20)

print('Seja bem vindo a votação para a escolha do Presidente da República Federativa do Bostil!\n'
      'Pelos próximos quatro anos, um desses estelionatários vai te roubar até você não aguentar mais;\n'
      'Te darei os números dos candidatos para você escolher essas pérolas:\n'
      '------------------------------\n'
      'Ex-presidiário     (PT):  1\n'
      'Futuro-presidiário (PL):  2\n'
      'Calvo              (PDT): 3\n'
      'Quem é esse cara?  (PNL): 4\n'
      'Nulo                    : 5\n'
      'Branco                  : 6\n'
      '------------------------------\n')

conttotal = contlula = contbolso = contciro = contrandom = contnulo = contbranco = 0
escolha = 1
while escolha != 0:
      escolha = int(input("Digite sua escolha (0 para parar): "))
      while escolha < 0 or escolha > 6:
            escolha = int(input("ERRO! Digite sua escolha entre (0 e 6): "))
      if escolha != 0:
            conttotal += 1
      if escolha in range(1, 7):
            print("Computando voto...")
            sleep(2)
      if escolha == 1:
            contlula +=1 
      elif escolha == 2:
            contbolso += 1
      elif escolha == 3:
            contciro += 1
      elif escolha == 4:
            contrandom += 1
      elif escolha == 5:
            contnulo += 1
      elif escolha == 6:
            contbranco += 1
      elif escolha == 0:
            break

print(f"Total de votos: {conttotal};\n"
      f"Total de votos (Ex-presidiário)    : {contlula};\n"
      f"Total de votos (Futuro-presidiário): {contbolso};\n"
      f"Total de votos (Calvo)             : {contciro};\n"
      f"Total de votos (Quem é esse cara?) : {contrandom};\n"
      f"Total de votos (Branco)            : {contbranco};\n"
      f"Total de votos (Nulo)              : {contnulo};\n"
      f"Porcentagem de votos nulos em cima do total: {(contnulo/conttotal)*100:.2f}%;\n"
      f"Porcentagem de votos em branco em cima do total: {(contbranco/conttotal)*100:.2f}%;\n")
