"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento."""

import math

populacaoA = 80000
taxaA = 0.03

populacaoB = 200000
taxaB = 0.015

tempo = 0
while populacaoA < populacaoB:
    crescimentoA = populacaoA * taxaA
    populacaoA = populacaoA + crescimentoA
    crescimentoB = populacaoB * taxaB
    populacaoB = populacaoB + crescimentoB
    tempo += 1

if populacaoA == populacaoB:
    print(f"As duas populações se equipararam em {tempo} anos e estão em {math.floor(populacaoA)} habitantes.")
else:
    print(f"A população do país A precisou de {tempo} anos para superar a população do país B.")
    print(f"As duas populações estão em {math.floor(populacaoA)} habitantes para o país A e {math.floor(populacaoB)} "
          f"habitantes para o país B.")
