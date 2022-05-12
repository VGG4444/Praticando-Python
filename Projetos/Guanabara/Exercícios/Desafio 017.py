# ler os catetos de um triângulo retângulo e calcular a hipotenusa

from math import pow, sqrt

catetoA = float(input("Informe o comprimento do cateto adjacente: "))
catetoB = float(input("Informe o comprimento do cateto oposto: "))

hipotenusa2 = (pow(catetoA, 2)) + (pow(catetoB, 2))
hipotenusa = sqrt(hipotenusa2)

print(f"O triângulo retângulo com catetos de comprimento {catetoA} e {catetoB} tem hipotenusa de {hipotenusa:.1f}")
