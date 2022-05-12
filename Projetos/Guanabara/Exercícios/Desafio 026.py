# Ler uma frase e mostrar quantas vezes a letra "a" aparece, a posição que aparece da primeira vez e na última

frase = input("Digite uma frase: ").lower().strip()

print(frase.count('a'))
cA = frase.find('a')
print(cA)
print(frase.rfind('a'))
