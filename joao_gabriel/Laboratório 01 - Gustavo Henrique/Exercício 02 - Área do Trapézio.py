"""
     Laboratorio 01 - Exercício 02
          Área do Trapézio
"""

lab = 'Laboratório 01'
frase = 'Área do Trapézio'
print('-=' * 30, '\n' + f'{lab:^60}' '\n' + f'{frase:^60}' '\n' + '-=' * 30)

base_menor = 4
base_maior = 6
altura = 5
area_do_trapezio = ((base_maior+base_menor)*altura)/2

print(f'A área do trapézio é: {area_do_trapezio} metros.')
