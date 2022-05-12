# leia uma velocidade de carro, se for maior que 80, calcule uma multa de 7 reais por km acima do limite

multa = 0

velocidade = int(input("Informe a velocidade do carro em km/h: "))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print(f"Você foi multado! A sua multa é de R${multa}!")
else:
    print("Você está dentro dos limites de velocidade!")
