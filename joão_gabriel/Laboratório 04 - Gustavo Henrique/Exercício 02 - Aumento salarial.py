"""
  Laboratório 04
   Exercício 02
"""

salario = float(input("Qual é o valor do seu salário? R$"))
print("Seu novo salário é de R$", end='')
if salario < 2000:
  novo_salario = (salario * 1.1) + 200
  print(f"{novo_salario:.2f}")
elif salario < 5000:
  novo_salario = (salario * 1.08) + 150
  print(f"{novo_salario:.2f}")
else:
  novo_salario = salario * 1.05
  print(f"{novo_salario:.2f}")
