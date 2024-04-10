"""Exercício 01 - Radar de velocidade"""
"""
Escreva um programa que peça a velocidade de um carro. Caso ultrapasse 80 km/h,
exiba uma mensagem com o valor da multa. Calcule R$ 5,00 para cada km que
exceder os 80 km/h.
"""

v = float(input('Qual foi a velocidade do carro? '))
print(f'Sua velocidade foi {v} km/h e você está ', end='')
print(f'acima da velocidade permitida, por isso terá que pagar uma multa de R${(v - 80) * 5}.' 
      if v > 80 else f'dentro da velocidade permitida, boa viagem!')
