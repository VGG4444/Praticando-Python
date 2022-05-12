# sorteie uma ordem de 4 grupos

from random import shuffle

a1 = input("Informe um aluno: ")
a2 = input("Informe um aluno: ")
a3 = input("Informe um aluno: ")
a4 = input("Informe um aluno: ")
lista = [a1, a2, a3, a4]
shuffle(lista)
print(lista)
