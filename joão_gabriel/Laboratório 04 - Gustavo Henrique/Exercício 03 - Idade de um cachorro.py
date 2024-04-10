"""
  Laboratório 04
   Exercício 03
"""

idade = float(input(f"Quantos anos, humanos, de vida seu cachorro tem? "))
print(f"Seu cachorro tem ", end='')
if idade < 3:
  anos_dog = 10.5 * idade
  print(f'{anos_dog} anos.')
else:
  anos_dog = (10.5 * 2) + ((idade - 2) * 4)
  print(f'{anos_dog} anos.')
