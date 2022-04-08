"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares."""

pares = list(())
impares = list(())

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    pares.append(numero) if (numero % 2 == 0) else impares.append(numero)

print("\nDos números digitados: ")
print(f"- São pares {pares}")
print(f"- São ímpares {impares}")
