"""O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por
item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado."""


print("CONSUMAÇÃO DA LANCHONETE")

cardapio = {100: {"produto": "Cachorro Quente", "preco": 1.2}, 101: {"produto": "Bauru Simples", "preco": 1.3},
            102: {"produto": "Bauru Com Ovo", "preco": 1.5}, 103: {"produto": "Hamburguer", "preco": 1.2},
            104: {"produto": "Cheeseburguer", "preco": 1.3}, 105: {"produto": "Refrigerante", "preco": 1.0}}

total = 0
encerrar = "N"
produtosConsumidos = {}

while encerrar == "N":
    codigo = int(input("\nCódigo: "))
    quantidade = int(input("Quantidade: "))

    if codigo in cardapio.keys():
        produto = cardapio[codigo]["produto"]
        preco = cardapio[codigo]["preco"]
        valorPorProduto = preco * quantidade
        total += valorPorProduto
        produtosConsumidos[produto] = valorPorProduto

    else:
        print("Produto não cadastrado")

    encerrar = (input("Deseja fechar a conta (S/N)? ")).upper()


print("\nCONTA")
print("-------------------------------------")

for x, y in produtosConsumidos.items():
    print("{}    R$ {}".format(x, y))

print("-------------------------------------")
print("Total: R$ {:.2f}".format(total))
