"""Faça um programa que calcule o mostre a média aritmética de N notas."""

notas = list(())
numero = 0
while numero >= 0:
    numero = float(input("Insira o valor da nota: "))
    
    if numero >= 0:
        notas.append(numero)
        media = sum(notas) / len(notas)
        print(f"A média dos números digitados é {media} pontos.")
    else:
        print("A nota precisa ser maior do que zero.")
