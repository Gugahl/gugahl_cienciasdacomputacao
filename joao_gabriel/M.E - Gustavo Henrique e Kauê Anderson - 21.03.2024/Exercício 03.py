"""Exercício 03"""
"""
Crie um programa que deve receber do usuário uma palavra de pelo menos 4
letras minúsculas e então converter cada uma destas letras para sua versão
maiúscula, printar o resultado, e então converter esta palavra em uma senha
numérica. Esta senha numérica é composta pelo ordinal de cada uma das
letras maiúsculas que compõem a palavra, concatenados.
Ex: Entrada: joao Saída: JOAO
                        74796579
"""

palavra = input("Digite uma palavra minúscula de exatamente 4 letras: ")
palavra_maiuscula = chr(ord(palavra[0]) - 32) + chr(ord(palavra[1]) - 32) + chr(ord(palavra[2]) - 32) + chr(ord(palavra[3]) - 32)
print(f'A palavra foi {palavra} e em caixa alta ficou {palavra_maiuscula}')
senha = f'{ord(palavra[0]) - 32}' + f'{ord(palavra[1]) - 32}' + f'{ord(palavra[2]) - 32}' + f"{ord(palavra[3]) - 32}"
print(f'A senha criada foi: {senha}')
