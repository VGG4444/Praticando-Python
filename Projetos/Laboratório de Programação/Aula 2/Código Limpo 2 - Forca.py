erros = 0
sCerto = False
oCerto = False
lCerto = False

while True:
    tentativa = input("Digite uma letra: ").lower()

    if tentativa == "s":
        print("S__")
        sCerto = True
    if tentativa == "o":
        print("_O_")
        oCerto = True
    if tentativa == "l":
        print("__L")
        lCerto = True

    if sCerto and oCerto is True:
        print("SO_")
    if sCerto and lCerto is True:
        print("S_L")
    if oCerto and lCerto is True:
        print("_OL")

    if sCerto and oCerto and lCerto is True:
        print("SOL!")
        print("Você acertou!")
        break

    if tentativa != "s" or "o" or "l":
        erros += 1
    if erros == 3:
        print("Você errou demais!")
        break
