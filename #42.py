"""Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo."""

print("CONTADOR DE NÚMEROS INTEIROS")
print("Digite números entre 0 e 100\n")

umQuarto = 0
doisQuartos = 0
tresQuartos = 0
quatroQuartos = 0
numero = 0

while numero >= 0:
    numero = int(input("Número: "))

    if numero in range(0, 26):
        umQuarto += 1
    elif numero in range(26, 51):
        doisQuartos += 1
    elif numero in range(51, 76):
        tresQuartos += 1
    elif numero in range(76, 101):
        quatroQuartos += 1
    else:
        print("Número inválido!")


print(f"\nForam digitados {umQuarto} números entre 0 e 25.")
print(f"Foram digitados {doisQuartos} números entre 26 e 50.")
print(f"Foram digitados {tresQuartos} números entre 51 e 75.")
print(f"Foram digitados {quatroQuartos} números entre 76 e 100.")
