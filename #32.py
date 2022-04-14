"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""

"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""

numero = int(input("Escolha um número: "))
numeroMultiplicador = numero

fatorial = 1
i = 2
multiplicadores = [numero]

while i <= numero:
    fatorial = fatorial * i
    i += 1
    numeroMultiplicador -= 1
    multiplicadores.append(numeroMultiplicador)

print(f"\nFatorial de: {numero}")
multiplicadoresStr = (str(multiplicadores)[1:-1]).replace(", ", " . ")
print(f"{numero}! = {multiplicadoresStr} = {fatorial}")
