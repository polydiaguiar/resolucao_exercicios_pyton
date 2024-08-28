#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Avalie o curso com nota de 0 a 10: "))

while True:

    if (nota<0) or (nota>10):
        nota = float(input("Valor invalido. Avalie novamente: "))
    else:
        print("Obrigada por avaliar!")
        break
