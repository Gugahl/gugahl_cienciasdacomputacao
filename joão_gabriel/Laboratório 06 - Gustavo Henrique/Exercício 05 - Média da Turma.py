"""Exercício 05 - Média da Turma"""
"""
Crie um programa em que você deve receber as notas de 5 alunos de uma
turma e imprimir ao final apenas as notas que estiverem acima (ou igual) à
média da turma.
Exemplo:
Entrada: 2
6
10
5
7
Saída: A média dos 5 alunos foi 6.0, e as notas igual ou acima da
média são: [6, 10, 7]
"""

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
notas_acima_media = [nota for nota in notas if nota >= media]

print(f"A média dos 5 alunos foi {media:.1f}, e as notas igual ou acima da média são: {notas_acima_media}")

