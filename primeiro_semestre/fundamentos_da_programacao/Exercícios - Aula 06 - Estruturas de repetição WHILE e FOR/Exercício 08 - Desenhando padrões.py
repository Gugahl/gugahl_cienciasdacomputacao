"""Exercício 08 - Desenhando padrões"""
"""
Escreva um programa para desenhar o seguinte padrão a depender do valor passado
(No exemplo abaixo o valor é 5).
"""

"""
num = int(input("Digite um número inteiro: "))
cont = 1
cont2 = num - 1
asterisco = '* '
soma = asterisco
subtracao = cont2 * asterisco

print('')
while cont != num + 1:
    cont += 1
    print(soma)
    soma += asterisco

while cont2 != 0:
    print(subtracao)
    cont2 -= 1
    subtracao = cont2 * asterisco
print('')
"""

"""
n = int(input("Me forneça o número máximo de '*' para construir o padrão: "))
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print("")

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print("")
"""
