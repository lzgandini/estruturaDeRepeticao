"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

lista = list(())
soma = 0

for indice in range(5):
    numero = float(input("Digite um número: "))
    lista.append(numero)

soma = sum(lista)
media = soma / len(lista)
print(f"\nAs notas informadas foram: {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}")
print(f"A soma das notas é {soma} e a média é {media} pontos.")
