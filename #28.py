"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e
 valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

cds = int(input("Quantos CDs você tem? "))
valores = list(())

for indice in range(cds):
    valorPorCd = float(input("Quanto custou o CD? "))
    valores.append(valorPorCd)

media = sum(valores) / cds

print("\nO valor médio gasto em cada CD foi R$ {:.2f}.".format(media))
