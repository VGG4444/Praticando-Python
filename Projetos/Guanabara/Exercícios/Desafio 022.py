# Ler um nome e mostrar todas as letras minúsculas, maiúsculas, quantas letras sem considerar espaços
# e quantas letras tem o primeiro nome

nome = input("Insira um nome: ")
nomeS = nome.split()

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(len(nomeS[0]))
