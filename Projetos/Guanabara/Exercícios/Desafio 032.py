# leia um número e diga se ele é bissexto

ano = int(input("Digite um ano: "))
calculo = ano % 4
if calculo == 0:
    print(f" O ano {ano} é um ano bissexto!")
else:
    print(f" O ano {ano} não é um ano bissexto!")