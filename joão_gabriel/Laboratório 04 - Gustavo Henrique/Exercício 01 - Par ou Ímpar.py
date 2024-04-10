"""
  Laboratório 04
   Exercício 01
"""

numero = int(input("Digite um número inteiro: "))
print(f'O número {numero} é ', end='')
if numero % 2 == 0:
  print("PAR.")
else:
  print("ÍMPAR.")
