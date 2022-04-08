"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

numero = 0
while numero >= 0 and numero <= 10:
    numero = int(input("Digite um número entre 0 e 10: "))

print("\nValor inválido.")
