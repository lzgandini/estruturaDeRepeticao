"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
I) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
II) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
III) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.

a) Faça um programa que determine o salário atual desse funcionário.
b) Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""

import datetime

# a)
#salarioInicial = 1000

# b)
salarioInicial = float(input("Informe o salário inicial do funcionário: "))
percentualDeAumento = 0.015
salarioAtual = salarioInicial + (salarioInicial * percentualDeAumento)

anoAtual = (datetime.datetime.now()).year

for indice in range(1997, anoAtual):
    percentualDeAumento = percentualDeAumento * 2
    salarioAtual = salarioAtual + (salarioAtual * percentualDeAumento)

print("Salário atual: {:.2f}".format(salarioAtual))
