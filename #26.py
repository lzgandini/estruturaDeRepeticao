"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

totalEleitores = int(input("Informe o número total de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
votoInvalido = 0

for indice in range(totalEleitores):
    voto = int(input("Informe seu voto (1- João, 2- Maria, 3- Laura): "))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        votoInvalido += 1

print(f"\nJoão recebeu {candidato1} votos, Maria {candidato2} votos e Laura {candidato3} votos.")
print(f"Foram computados {votoInvalido} votos inválidos.")

maisVotado = max(candidato1, candidato2, candidato3, votoInvalido)
if maisVotado == candidato1:
    vencedor = "é João"
elif maisVotado == candidato2:
    vencedor = "é Maria"
elif maisVotado == candidato3:
    vencedor = "é Laura"
else:
    vencedor = "não foi identificado"

print(f"\nO vencedor {vencedor} e recebeu {maisVotado} votos.")
