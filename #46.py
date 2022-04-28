"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m"""

encerrar = "N"

while encerrar == "N":
    nome = (input("\nNome do atleta: ")).title()
    primeiro = float(input("Primeiro salto: "))
    segundo = float(input("Segundo salto: "))
    terceiro = float(input("Terceiro salto: "))
    quarto = float(input("Quarto salto: "))
    quinto = float(input("Quinto salto: "))

    saltos = [primeiro, segundo, terceiro, quarto, quinto]
    maior = max(saltos)
    menor = min(saltos)

    for indice in saltos:
        if indice == maior:
            saltos.remove(indice)

    for indice in saltos:
        if indice == menor:
            saltos.remove(indice)

    media = sum(saltos) / len(saltos)

    print(f"\nAtleta: {nome}")
    print(f"Primeiro Salto: {primeiro} m")
    print(f"Segundo Salto: {segundo} m")
    print(f"Terceiro Salto: {terceiro} m")
    print(f"Quarto Salto: {quarto} m")
    print(f"Quinto Salto: {quinto} m")

    print(f"\nMelhor salto: {maior} m")
    print(f"Pior salto: {menor} m")
    print("Média dos demais saltos: {:.2f} m".format(media))

    print("\nResultado final:")
    print("{}: {:.2f} m".format(nome, media))

    encerrar = (input("Deseja encerrar o cadastro de saltos (S/N)? ")).upper()
