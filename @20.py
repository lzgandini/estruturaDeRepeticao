"""a) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
    b) Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
    fatorial a números inteiros positivos e menores que 16."""

numero = 0

while numero >= 0 and numero < 16 and isinstance(numero, int):
    numero = int(input("Escolha um número inteiro positivo e menor do que 16: "))

    if numero >= 0 and numero < 16 and isinstance(numero, int):
        fatorial = 1
        i = 2
        while i <= numero:
            fatorial = fatorial * i
            i += 1
        print(f"O valor de {numero} fatorial é {fatorial}.")
    else:
        break

print(f"O número {numero} é inválido.")
