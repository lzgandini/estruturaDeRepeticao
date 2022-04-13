"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas
e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""

import math

turmas = int(input("Digite a quantidade de turmas: "))
totalDeAlunos = list(())

for indice in range(turmas):
    alunos = int(input("Digite a quantidade de alunos da turma: "))

    if alunos <= 40:
        totalDeAlunos.append(alunos)
    else:
        print("Número de alunos excede o permitido. Não considerarei esta uma turma.")

media = sum(totalDeAlunos) / len(totalDeAlunos)

print(f"O número médio de alunos por turma é {math.floor(media)}.")
