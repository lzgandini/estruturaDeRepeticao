"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""

nome = input("Informe seu nome de usuário: ")
senha = input("Informe sua senha (diferente do nome): ")

while nome == senha:
    print("\nSeu nome de usuário e senha devem ser diferentes. Vamos de novo!\n")
    nome = input("Informe seu nome de usuário: ")
    senha = input("Informe sua senha (diferente do nome): ")

print(f"\nObrigada {nome}!")
