"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
intervalo compreendido por eles."""

import random

max = int(input("Digite um número inteiro: "))
min = int(input("Digite outro número inteiro: "))

numeroRandomico = random.randint(max, min)

print(f"O número sorteado é {numeroRandomico}.")
