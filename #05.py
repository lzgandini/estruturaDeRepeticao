"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação."""

import math

populacaoA = float(input("Informe a população inicial da primeira cidade: "))
porcentagemA = float(input("Qual é a taxa de crescimento anual desta cidade (em %)? "))
taxaA = porcentagemA / 100

populacaoB = float(input("Informe a população inicial da segunda cidade: "))
porcentagemB = float(input("Qual é a taxa de crescimento anual desta cidade (em %)? "))
taxaB = porcentagemB / 100

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
