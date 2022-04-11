"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""

numero = int(input("Escolha um número: "))

fatorial = 1
i = 2

while i <= numero:
    fatorial = fatorial * i
    i += 1

print(f"O valor de {numero} fatorial é {fatorial}.")
