"""Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são
informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

encerrar = "N"
notas = []

while encerrar == "N":
    nome = (input("\nNome do atleta: ")).title()

    for indice in range(7):
        nota = float(input("Nota: "))
        notas.append(nota)

    maior = max(notas)
    menor = min(notas)

    for indice in notas:
        if indice == maior:
            notas.remove(indice)

    for indice in notas:
        if indice == menor:
            notas.remove(indice)

    media = sum(notas) / len(notas)

    print(f"\nAtleta: {nome}")

    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {maior} m")
    print(f"Pior nota: {menor} m")
    print("Média: {:.2f} m".format(media))

    notas = []
    encerrar = (input("\nDeseja encerrar o cadastro de saltos (S/N)? ")).upper()
