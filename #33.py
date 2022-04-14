"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""

temperaturas = list(())
i = 0

while i < 10:
    temperaturaAtual = float(input("\nInforme a temperatura atual: "))
    temperaturas.append(temperaturaAtual)
    maior = max(temperaturas)
    menor = min(temperaturas)
    media = sum(temperaturas) / len(temperaturas)

    print(f"A maior temperatura registrada foi {maior} graus.")
    print(f"A menor temperatura registrada foi {menor} graus.")
    print("A média das temperaturas registradas é {:.2f} graus.".format(media)) 
