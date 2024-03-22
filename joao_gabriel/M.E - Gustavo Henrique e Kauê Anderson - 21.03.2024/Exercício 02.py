"""Exercício 02"""
"""
Crie um programa que deve receber uma string do usuário e logo em seguida
recebe 2 inteiros que correspondem à posições dentro desta string. Ao fim
imprima a substring entre os 2 números escolhidos.
"""

palavra = input("Digite uma palavra: ")
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
res = palavra[num1:num2]
print(res)
