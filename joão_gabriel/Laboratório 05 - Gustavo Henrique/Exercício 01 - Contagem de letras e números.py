"""Exercício 01 - Contagem de letras e números"""
"""
1) Crie um programa que deve receber do usuário uma string (sem espaços)
contendo letras e números e então printar em uma linha apenas as letras
contidas na string e na outra apenas os números, na ordem que elas se
encontram na string original. Dica: use o atributo de strings isnumeric().
Entrada: A23bC7 Saída: Characteres: AbC
Números: 237
"""

exercicio = 'Exercício 01 - Contagem de letras e números'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30 + f'\n')

frase = input('Digite algo: ')
frase = frase.replace(' ', '')
cont = len(frase) - 1
teste = numer = strin = ' '
while cont >= 0:
    teste = frase[cont].isnumeric()
    print(end='')
    if teste == True:
        numer += f'{frase[cont]}'
    else:
        strin += f'{frase[cont]}'
    cont -= 1
print(f'Letras: {strin[::-1].strip()}')
print(f'Números: {numer[::-1].strip()}')
