"""Exercício 03 - Criação de senhas"""
"""
Crie um programa que deve checar a validade de uma senha. O usuário deve
entrar com uma senha e o programa só é concluído caso a senha seja válida,
senão o pedido de uma nova senha é repetido. Para que a senha seja válida
ela precisa seguir as regras abaixo:
a) Ter no mínimo 8 e no máximo 16 caracteres.
b) Ter ao menos 1 número.
c) Ter ao menos uma letra.
Entrada: cleiton Saída: Senha inválida!
cleitinho Senha inválida!
cleitinho07 Senha válida!
"""

exercicio = 'Exercício 03 - Criação de senhas'
print(f'=-' * 30 + f'\n' + f'{exercicio:^60}' + f'\n' + f'=-' * 30)

print("""Crie uma senha que siga os requisitos abaixo:
a) Ter no mínimo 8 e no máximo 16 caracteres;
b) Ter ao menos 1 número;
c) Ter ao menos uma letra.\n""")

senha = input("Senha: ")
senha = senha.replace(' ', '')
cont = len(senha)
pos = numero = letra = 0
while pos < cont:
    caractere = ord(senha[pos])
    if caractere in range(65, 91) or caractere in range(97, 123):
        letra += 1
    if caractere in range(48, 58):
        numero += 1
    pos += 1
if letra >= 1 and numero >= 1 and cont > 7 and cont < 17:
    print(f'Senha válida!')
else:
    print(f'Senha inválida!')
