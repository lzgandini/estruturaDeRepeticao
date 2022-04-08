"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""

pares = list(())

for i in range(50):
    if i % 2 == 0:
        pares.append(i)

print(f"O números pares entre 1 e 50 são {pares}.")
