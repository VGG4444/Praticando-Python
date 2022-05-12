# gerar 5 números, colocar numa tupla, mostrar e dizer qual o maior e o menor

from random import randint


a1 = randint(0, 10)
a2 = randint(0, 10)
a3 = randint(0, 10)
a4 = randint(0, 10)
a5 = randint(0, 10)

maior = a1
if a2 > maior:
    maior = a2
if a3 > maior:
    maior = a3
if a4 > maior:
    maior = a4
if a5 > maior:
    maior = a5

menor = a1
if a2 < menor:
    menor = a2
if a3 < menor:
    menor = a3
if a4 < menor:
    menor = a4
if a5 < menor:
    menor = a5


tupla = (a1, a2, a3, a4, a5)

print(f"Os números foram: {tupla}.\n"
      f"O maior número foi: {maior}\n"
      f"O menor número foi: {menor}")
