# ler quatro números e mostrar quantas vezes 9 apareceu, a posição do número 3, quais os números pares

contador9 = 0
contadorPar = 0

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

tupla = (n1, n2, n3, n4)

if 9 in tupla:
    contador9 += 1
print(f"O número 9 apareceu {contador9} vezes.")

if 3 in tupla:
    print(f"O número 3 aparece na posição {tupla.index(3)+1}")
else:
    print(f"Não existe 3 nesses números.")

if n1 % 2 == 0:
    contadorPar += 1
if n2 % 2 == 0:
    contadorPar += 1
if n3 % 2 == 0:
    contadorPar += 1
if n4 % 2 == 0:
    contadorPar += 1
print(f"Existem {contadorPar} números pares.")
