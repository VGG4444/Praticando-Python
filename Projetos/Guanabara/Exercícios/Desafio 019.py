# sorteie um de quatro alunos

from random import randint

sorteado = "ninguém"

a1 = input("Informe o primeiro aluno: ")
a2 = input("Informe o segundo aluno: ")
a3 = input("Informe o terceiro aluno: ")
a4 = input("Informe o quarto aluno: ")

sorteio = randint(1, 4)

if sorteio == 1:
    sorteado = a1
if sorteio == 2:
    sorteado = a2
if sorteio == 3:
    sorteado = a3
if sorteio == 4:
    sorteado = a4

print(f"O aluno sorteado foi {sorteado}")
