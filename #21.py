"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

numero = 0

while isinstance(numero, int):
    numero = int(input("Digite um número inteiro: "))

    numeroUm = numero != 1
    multiploDeDois = numero != 2 and numero % 2 == 0
    multiploDeTres = numero != 3 and numero % 3 == 0
    multiploDeCinco = numero != 5 and numero % 5 == 0
    multiploDeSete = numero != 5 and numero % 7 == 0

    if numeroUm or multiploDeDois or multiploDeTres or multiploDeCinco or multiploDeSete:
        print(f"{numero} não é um número primo.")
    else:
        print(f"{numero} é um número primo.")
