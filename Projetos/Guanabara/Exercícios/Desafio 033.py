# Digite três números e diga qual é o maior e qual o menor entre eles
maior = 0
menor = 99999

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if maior < n1:
    maior = n1
if maior < n2:
    maior = n2
if maior < n3:
    maior = n3

if menor > n1:
    menor = n1
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3

print(f"O maior número foi {maior} e o menor foi {menor}")
