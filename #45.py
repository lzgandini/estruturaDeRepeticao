"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões. O programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota 
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai 
utilizar o sistema. Após todos os alunos terem respondido informar:
a) Maior e Menor Acerto;
b) Total de Alunos que utilizaram o sistema;
c) A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos 
alunos usarem o programa."""

gabarito = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "e", 7: "d", 8: "c", 9: "b", 10: "a"}

respostas = {}
acertos = 0
acertosPorAluno = {}
encerrar = "N"

while encerrar == "N":
    nome = (input("\nQual é o seu nome? ")).capitalize()
    for indice in range(1, 11):
        letra = (input(f"Qual letra você marcou na {indice}? ")).lower()
        respostas[indice] = letra

        if gabarito[indice] == respostas[indice]:
            acertos += 1
            acertosPorAluno[nome] = acertos
    encerrar = (input("\nDeseja encerrar o cadastro (S/N)? ")).upper()
    acertos = 0

menorNota = min(acertosPorAluno.values())
maiorNota = max(acertosPorAluno.values())
totalDeAlunos = len(acertosPorAluno)
media = sum(acertosPorAluno.values()) / totalDeAlunos

print(f"\nMaior nota: {maiorNota}")
print(f"Menor nota: {menorNota}")
print(f"Total de alunos: {totalDeAlunos}")
print("Média da turma: {:.2f}".format(media))
print(f"\nTodas as notas: {acertosPorAluno}")
