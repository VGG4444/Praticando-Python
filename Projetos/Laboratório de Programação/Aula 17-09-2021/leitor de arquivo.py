with open('relatório.txt', 'r') as lendo:
    i = 1
    for x in lendo:
        linha = x[:-1]
        print(f"Linha {i}: {linha}")
        i += 1
        input("Deseja limpar o arquivo? ")

