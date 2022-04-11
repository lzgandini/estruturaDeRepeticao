"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

quantasVezes = int(input("Informe a quantidade de números que você deseja comparar: "))
lista = list(())

for i in range(quantasVezes):
    numero = int(input("Digite um número: "))
    lista.append(numero)

maior = max(lista)
menor = min(lista)
soma = sum(lista)

print(f"\nO maior número inserido foi {maior}.")
print(f"O menor número inserido foi {menor}.")
print(f"A soma de todos os números inseridos é {soma}.")
