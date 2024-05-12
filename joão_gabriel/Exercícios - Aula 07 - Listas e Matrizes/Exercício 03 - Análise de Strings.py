"""Exercício #03 - Análise de Strings"""
"""
Escreva um programa para contar em uma lista de strings quantas têm mais de 2
caracteres e começam e terminam com o mesmo caractere.
"""

lista = ["Felipe", "Davi", "Santos", "Luiz"]
doiscaracteres = 0

exercicio = 'Exercício #03'
print(f'-=' * 15 + f'\n' + f'{exercicio:^30}' + f'\n' + f'-=' * 15)

for string in lista:
  string = string.lower()
  if len(string) > 2 and string[0] == string[-1]:
    doiscaracteres += 1
print(f'Existem {doiscaracteres} strings com mais de 2 caracteres e que começam\n'
      f'e terminam com o mesmo caracter.')
