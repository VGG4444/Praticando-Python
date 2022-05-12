# faça o programa pensar num número de 1 a 5 e diga se o usuário adivinhou ou não

from random import randint

numero = int(input("Tente adivinhar o número de 0 a 5: "))
sorteio = randint(0, 5)
if numero == sorteio:
    print(f"Parabéns, você acertou! O número era {sorteio}")
else:
    print(f"Que pena, você errou! O número era {sorteio}")
