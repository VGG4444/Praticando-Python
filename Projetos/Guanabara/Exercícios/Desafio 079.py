lista = list()
while True:
    num = (int(input(f"Digite um número: ")))
    lista.append(num)
    re = input("Deseja continuar? (S/N) ").capitalize()
    cont = lista.count(num)
    if cont > 1:
        lista.remove(num)
    if re == "N":
        break
lista.sort()
print(lista)
