"""
  Laboratório 04
   Exercício 04
"""

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um número inteiro: "))
numero3 = int(input("Digite um número inteiro: "))
numero4 = int(input("Digite um número inteiro: "))
soma = numero3 + numero4
multiplicação = numero3 * numero4
print(f"A soma de {numero3} e {numero4}, que resulta em {soma}", end='')
print(f" está dentro da faixa." if numero1 < soma < numero2 else f' não está dentro da faixa.')
print(f"A multiplicação de {numero3} * {numero4}, que resulta em {multiplicação}", end='')
print(f" está dentro da faixa." if numero1 < multiplicação < numero2 else f' não está dentro da faixa.')
