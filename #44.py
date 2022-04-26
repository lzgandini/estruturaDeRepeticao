"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
a) O total de votos para cada candidato;
b) O total de votos nulos;
c) O total de votos em branco;
d) A percentagem de votos nulos sobre o total de votos;
e) A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero."""


candidatos = {1: {"nome": "Bolsonaro", "votos": 0}, 2: {"nome": "Lula", "votos": 0},
              3: {"nome": "Outro candidato", "votos": 0}, 4: {"nome": "Mais um candidato", "votos": 0},
              5: {"nome": "Votos nulos", "votos": 0}, 6: {"nome": "Em branco", "votos": 0}}

encerrar = "N"
totalDeVotos = 0

while encerrar == "N":
    voto = int(input("Digite o seu voto: "))

    if voto in candidatos.keys():
        candidatos[voto]["votos"] += 1
        totalDeVotos += 1
    else:
        print("Voto inválido")

    encerrar = (input("Deseja encerrar a votação (S/N)? ")).upper()

print("\nCONTAGEM DE VOTOS")
print("-------------------------------------")
for x, y in candidatos.items():
    print(f"{y}")
    if y["nome"] == "Votos nulos":
        porcentagemNulos = (y["votos"] / totalDeVotos) * 100
    if y["nome"] == "Em branco":
        porcentagemBrancos = (y["votos"] / totalDeVotos) * 100

print("\nPorcentagem de votos nulos: {:.1f}%".format(porcentagemNulos))
print("Porcentagem de votos brancos: {:.1f}%".format(porcentagemBrancos))
