"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';   """

nome = input("Informe seu nome: ")
while len(nome) < 3:
    print("\nSeu nome precisa ter mais do que três dígitos. Vamos de novo!\n")
    nome = input("Informe seu nome: ")

idade = int(input("Quantos anos você tem? "))
while idade < 0 or idade > 150:
    print("\nTo achando meio estranha essa sua idade! Você digitou o número certo?\n")
    idade = int(input("Digite um número entre 0 e 150 anos: "))

salario = float(input("Quanto você ganha por mês? "))
while salario < 0:
    print("\nDigite zero caso você não receba nenhum salário. Esse é o valor mínimo que posso registrar.\n")
    salario = float(input("Quanto você ganha por mês? "))

genero = (input("Informe seu gênero (H - homem, M - mulher, O - outro, N - prefiro não informar): ")).upper()
opcoesDeGenero = "HMON"
while genero not in opcoesDeGenero:
    print("Informação inválida. Vamos de novo!")
    genero = (input("Informe seu gênero (H - homem, M - mulher, O - outro, N - prefiro não informar): ")).upper()

if genero == opcoesDeGenero[0]:
    genero = "Homem"
elif genero == opcoesDeGenero[1]:
    genero = "Mulher"
elif genero == opcoesDeGenero[2]:
    genero = "Outro"
else:
    genero = "Prefiro não informar"

estadoCivil = (input("Qual é o teu estado civil (S - solteiro, C - casado, V - viúvo, D - divorciado): ")).upper()
opcoesDeEstadoCivil = "SCVD"
while estadoCivil not in opcoesDeEstadoCivil:
    print("Informação inválida. Vamos de novo!")
    estadoCivil = (input("Qual é o teu estado civil (S - solteiro, C - casado, V - viúvo, D - divorciado): ")).upper()

if estadoCivil == opcoesDeEstadoCivil[0]:
    estadoCivil = "Solteiro"
elif estadoCivil == opcoesDeEstadoCivil[1]:
    estadoCivil = "Casado"
elif estadoCivil == opcoesDeEstadoCivil[2]:
    estadoCivil = "Viúvo"
else:
    estadoCivil = "Divorciado"

print("\nDADOS PESSOAIS")
print(f"Nome: {nome.title()}")
print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario}")
print(f"Gênero: {genero}")
print(f"Estado Civil: {estadoCivil}")
