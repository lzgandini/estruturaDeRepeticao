"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média
de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada."""

numeroPessoas = int(input("Informe o número de pessoas que participarão da pesquisa: "))
idades = list(())

for indice in range(numeroPessoas):
    idade = int(input("Digite a idade de pessoa: "))
    idades.append(idade)

media = sum(idades) / len(idades)

if media <= 25:
    print("A turma é jovem, pois a média das idades é {:.2f}.".format(media))
elif media > 25 and media <= 60:
    print("A turma é adulta, pois a média das idades é {:.2f}.".format(media))
else:
    print("A turma é idosa, pois a média das idades é {:.2f}.".format(media))
