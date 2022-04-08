"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem."""

base = int(input("Digite a base do cálculo de potência: "))
expoente = int(input("Qual é o expoente? "))
potencia = base

#SOLUCAO 1
for i in range(1, expoente):
    potencia = potencia * base

"""
#SOLUCAO 2
potencia = base ** expoente

#SOLUCAO 3
potencia2 = pow(base, expoente)
"""

print(f"{base} elevado à {expoente} = {potencia}")
