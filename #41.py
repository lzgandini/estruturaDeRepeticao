"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67"""


divida = float(input("Qual é o valor da dívida? "))
parcelas = {1: 0, 3: 0.1, 6: 0.15, 9: 0.20, 12: 0.25}

juros = {1: (divida * parcelas[1]), 3: (divida * parcelas[3]), 6: (divida * parcelas[6]),
         9: (divida * parcelas[9]), 12: (divida * parcelas[12])}

valorTotal = {1: (divida + juros[1]), 3: (divida + juros[3]), 6: (divida + juros[6]),
              9: (divida + juros[9]), 12: (divida + juros[12])}

print("\nValor da Dívida  Valor dos juros  Quantidade de Parcelas  Valor da Parcela")
print("R$ {}         {}                     1                 R$ {:.2f} ".format(valorTotal[1], juros[1], valorTotal[1]))
print("R$ {}         {}                   3                 R$ {:.2f} ".format(valorTotal[3], juros[3], valorTotal[3] / 3))
print("R$ {}         {}                   6                 R$ {:.2f} ".format(valorTotal[6], juros[6], valorTotal[6] / 6))
print("R$ {}         {}                   9                 R$ {:.2f} ".format(valorTotal[9], juros[9], valorTotal[9] / 9))
print("R$ {}         {}                  12                 R$ {:.2f} ".format(valorTotal[12], juros[12], valorTotal[12] / 12))
