"""Exercício 06 - Erros de usuário"""
"""
Refaça o programa da questão anterior, porém adicione uma proteção contra entradas
errôneas do usuário (Por exemplo, o programa não pode receber uma string onde deveria
receber um número). Quando um usuário entrar com uma entrada inválida, apresente uma
mensagem de erro e requisite que o valor seja inserido novamente até que todos os valores
necessários sejam inseridos.
"""
"""
num = input("Digite o número de valores a ser recebido: ")
soma = 0
while num.isnumeric() == False:
    num = input("Digite o número de valores a ser recebido: ")

if num.isnumeric() == True:
    num = int(num)
    for c in range(1, num + 1):
        n = float(input(f"Digite o {c}º número: "))
        soma += n
    print(f'A média entre os {num} valores recebidos foi {(soma/num):.2f}.')
"""

"""
num = input("Digite o número de valores a ser recebido: ")
soma = cont = 0
while num.isnumeric() == False:
    num = input("Digite o número de valores a ser recebido: ")

if num.isnumeric() == True:
    num = int(num)
    while cont != num:
        cont += 1
        n = float(input(f"Digite o {cont}º número: "))
        soma += n
    print(f'A média entre os {num} valores recebidos foi {(soma/num):.2f}.')
"""
