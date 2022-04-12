"""a) Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
    b) Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

quantasVezes = int(input("Informe a quantidade de números que você deseja comparar (até 1.000): "))
lista = list(())

if quantasVezes <= 1000:
    for i in range(quantasVezes):
        numero = int(input("Digite um número: "))
        lista.append(numero)

    maior = max(lista)
    menor = min(lista)
    soma = sum(lista)

    print(f"\nO maior número inserido foi {maior}.")
    print(f"O menor número inserido foi {menor}.")
    print(f"A soma de todos os números inseridos é {soma}.")
else:
    print("Valor inválido")
