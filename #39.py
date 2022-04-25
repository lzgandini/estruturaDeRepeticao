"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e
o número do aluno mais baixo, junto com suas alturas."""

dados = {}

for indice in range(3):
    numero = int(input("Número do aluno: "))
    altura = int(input("Altura em centímetros: "))
    dados[numero] = altura

maior = max(dados.values())
menor = min(dados.values())

for indice in dados:
    if dados[indice] == maior:
        print("\nAluno mais alto")
        print(f"Número: {indice} - Altura: {dados[indice]} centímetros")

    if dados[indice] == menor:
        print("\nAluno mais baixo")
        print(f"Número: {indice} - Altura: {dados[indice]} centímetros")
