#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input("Digite seu nome: "))
senha = str(input("Agora escolha uma senha:"))

while True:
    if nome == senha:
        senha = str(input("Digite uma nova senha diferente de seu nome: "))
    else:    
        print("Dados válidos.")
        break

