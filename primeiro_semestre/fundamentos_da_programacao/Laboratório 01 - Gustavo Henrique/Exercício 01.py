"""
     Laboratorio 01 - Exercício 01
          Graus para Radianos
"""

#  Deixando o código mais bonito
lab = 'Laboratório 01'
frase = 'Transformando Graus em Radianos'
print('-=' * 30, '\n' + f'{lab:^60}' '\n' + f'{frase:^60}' '\n' + '-=' * 30)

#  Variáveis preestabelecidas
pi = 3.14
trinta_em_radianos = (30/180) * pi
sessenta_em_radianos = (60/180) * pi
noventa_em_radianos = (90/180) * pi
cento_e_oitenta_em_radianos = (180/180) * pi

#  Printando os resultados
print(f'Para um ângulo de 30°, seu valor em radianos será: {trinta_em_radianos:.2f};\n'
      f'Para um ângulo de 60°, seu valor em radianos será: {sessenta_em_radianos:.2f};\n'
      f'Para um ângulo de 90°, seu valor em radianos será: {noventa_em_radianos:.2f};\n'
      f'Para um ângulo de 180°, seu valor em radianos será: {cento_e_oitenta_em_radianos:.2f}.')
