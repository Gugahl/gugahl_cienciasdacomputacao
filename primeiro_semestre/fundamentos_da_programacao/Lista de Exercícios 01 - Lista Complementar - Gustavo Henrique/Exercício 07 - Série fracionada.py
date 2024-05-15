"""Exercício 07 - Série fracionada"""
"""
Faça um programa que receba um inteiro n e dê a soma dos termos da série
a seguir: para n = 5, 1/1 + 2/3 + 3/5 + 4/7 + 5/9 = 3.393 (Aproxime para 3
casas decimais). A série é composta pelo numerador em ordem normal (1, 2,
3, 4, até n) e o denominador contendo apenas os números ímpares (1, 3, 5,
...)
"""

num = int(input("Digite um número inteiro: "))
c = n = d = soma = 0
while c < num:
    d += 1
    if d % 2 == 1:
        c += 1
        n += 1
        print(f'{n}/{d}', end='')
        print(f' + ' if c < num else f' = ', end='')
        soma += n/d
print(f'{(soma - 0.001):.3f}')
