"""Exercício 05 - Comparação de valores"""
"""
Faça um programa que, dado um conjunto de N números, determine o menor
valor, o maior valor e a soma dos valores. O N é recebido pelo usuário.
"""

qtd = float(input('Digite a quantidade de números a ser lida: '))
cont = maior = menor = soma = 0
while cont < qtd:
    cont += 1
    num = float(input('Digite um número: '))
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
print(f'Você digitou {qtd} valores, a soma entre eles resultou em {soma} sendo o maior valor {maior} e o menor valor {menor}.')
