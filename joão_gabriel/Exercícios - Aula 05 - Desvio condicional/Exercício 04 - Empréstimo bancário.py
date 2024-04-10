"""Exercício 04 - Empréstimo bancário"""
"""
Escreva um programa para aprovar o valor do empréstimo bancário de uma casa. O
programa deve perguntar o valor da casa, o salário e a quantidade de anos para realizar o
pagamento. O valor da prestação não deve ser superior a 30% do salário. Calcule o valor
da prestação como sendo o valor da casa dividido pelo número de meses no período
desejado. Diga se o valor superou os 30%, senão, imprima o valor da prestação.
"""

emprestimo = float(input("Qual é o valor do empréstimo que você quer? R$"))
salario = float(input("Qual é o valor do seu salário? R$"))
anos = int(input("Em quantos anos você deseja pagar esse empréstimo? "))
meses = anos * 12
prestacao = emprestimo/meses
if prestacao > (salario * 0.30):
    print("\033[31mEmpréstimo NEGADO!\033[m O valor da prestação supera 30% do seu salário.")
else:
    print(f'\033[32mEmpréstimo APROVADO!\033[m Você pagará {meses} prestações de R${prestacao:.2f}.')
