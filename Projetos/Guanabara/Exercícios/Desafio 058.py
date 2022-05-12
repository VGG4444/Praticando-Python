from random import randint

try:
    n = randint(1, 10)
    numero = 0
    contador = 0
    while n != numero:
        numero = int(input("Tente advinhar um número entre 1 e 10: "))
        contador += 1
    print(f"Você acertou! O número era {n}, e você acertou na {contador}º tentativa!")
except ValueError as numero:
    print("Digite um número válido!")
