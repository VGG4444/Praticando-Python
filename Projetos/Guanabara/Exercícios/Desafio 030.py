# leia um número e diga se ele é par ou impar

numero = int(input("Digite um número: "))
calculo = numero % 2
if calculo > 0:
    print("Esse número é impar!")

else:
    print("Esse número é par!")
