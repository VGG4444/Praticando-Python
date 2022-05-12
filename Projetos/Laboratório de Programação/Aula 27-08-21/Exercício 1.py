import random
from random import randint

numeros = []

def sorteio ():
    for i in range(6):
        num = randint(1, 60)
        while num in numeros:
            num = randint(1, 60)
        numeros.append(num)
    numeros.sort()
    return numeros

print(sorteio())
