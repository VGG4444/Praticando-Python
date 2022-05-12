matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
paresTc = []
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número para {l} e para {c}: "))
        if c == 2:
            if matriz[l][c] % 2 == 0:
                paresTc.append(matriz[l][c])
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print("*-"*20)
print(f"A soma dos valores pares da terceira coluna é: {sum(paresTc)}")
print(f"O maior valor da segunda linha é: {maior}")

