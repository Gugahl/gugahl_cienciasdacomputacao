"""Exercício 03 - Aumento salarial"""
"""
Escreva um programa que pergunta o salário do funcionário e calcula o valor do
aumento. Para salários superiores R$ 1.250,00 calcule 10% caso contrário 15%.
"""

salario = float(input("Qual é o valor do seu salário? R$"))
print("Seu novo salário é de R$", end='')
if salario < 1250:
  novo_salario = salario * 1.15
  print(f"{novo_salario:.2f}.")
else:
  novo_salario = salario * 1.1
  print(f"{novo_salario:.2f}.")
