nome = str(input("Digite um nome: "))
data = str(input("Digite a data de nascimento (Formato: DD/MM/AAAA): "))
dataC = 0
for i in data:
    dataC += 1
if dataC != 10:
    data = str(input("Digite uma data de nascimento válida! (Formato: DD/MM/AAAA): "))
cpf = str(input("Digite um número de CPF: "))
cpfC = 0
for i in cpf:
    cpfC += 1
if cpfC != 11:
    cpf = str(input("Digite um CPF válido! (Formato: DD/MM/AAAA): "))
credito = str(input("Digite o limite do cartão: "))
if credito[:2] != "R$":
    credito = str(input("Digite o limite do cartão com a moeda válida! (R$XXX): "))

print(nome.ljust(15, '-'))
print(data.ljust(15, '-'))
print(cpf.ljust(15, '-'))
print(credito.ljust(15, '-'))
