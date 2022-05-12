# Ler um número entre 0 e 9999 e dizer quais são os digitos separadamente

numero = int(input("Digite um número entre 0 e 9999: "))

print(numero // 1 % 10)
print(numero // 10 % 10)
print(numero // 100 % 10)
print(numero // 1000 % 10)
