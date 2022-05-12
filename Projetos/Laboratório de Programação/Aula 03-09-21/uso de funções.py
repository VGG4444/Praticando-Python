import imparparmedia


while True:
    numeroA = int(input("Digite um número: "))
    if numeroA == -1:
        break
    checkA = imparparmedia.impapar(numeroA)
    if checkA == "impar":
        print("Digite um número par!")
        break
    numeroB = int(input("Digite outro número: "))
    checkB = imparparmedia.impapar(numeroB)
    if checkB == "par":
        print("Digite um número impar!")
        break
    print(imparparmedia.media(numeroA, numeroB))
