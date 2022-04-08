"""Faça um programa que leia 5 números e informe o maior número."""

lista = list(())

for indice in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print(f"\nO maior número digitado foi {max(lista)}.")
