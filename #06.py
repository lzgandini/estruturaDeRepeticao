""" a) Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
b) Depois modifique o programa para que ele mostre os números um ao lado do outro."""

# a)
i = 1
while i <= 20:
    print(i)
    i += 1

# b)
lista = list(())
for i in range(1, 21):
    lista.append(i)

print(lista)
