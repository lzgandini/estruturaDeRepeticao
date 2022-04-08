""" a) Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
intervalo compreendido por eles.
b) Altere o programa anterior para mostrar no final a soma dos números."""

import random

# a)
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
numeros = [numero1, numero2]

min = min(numeros)
max = max(numeros)

numeroRandomico = random.randint(min, max)

print(f"O número sorteado é {numeroRandomico}.")

# b)
numeros = [min, max]
for i in range(min, max):
    numeros.append(i)

print(f"A soma dos números entre {min} e {max} é {sum(numeros)}")
