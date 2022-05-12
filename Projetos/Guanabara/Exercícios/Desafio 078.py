lista = list()
for i in range(0, 5):
    lista.append(int(input(f"Digite o número na posição {i}: ")))
maior = max(lista)
menor = min(lista)
print(f"O maior valor foi {maior} na posição {lista.index(maior)}")
print(f"O menor valor foi {menor} na posiçao {lista.index(menor)}")
