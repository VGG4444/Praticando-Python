# Leia a altura e largura de uma parede, calcule a área e diga quanta tinta é necessária para pintá-la

altura = float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))

area = largura * altura

print(f"A área da parede é de {area}m² e são necessários {area/2} litros de tinta")
