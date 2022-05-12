import calculodarea

print("Bem-vindo ao calculador de área!\n"
      "Escolha seu tipo de figura:\n"
      "1 - Retângulo\n"
      "2 - Triângulo\n"
      "3 - Círculo\n"
      "0 - Sair\n")

while True:
    tipo = int(input("Informe o tipo: "))
    if tipo == 0:
        print("Obrigado por usar!")
        break
    if tipo == 1:
        baseQ = float(input("Informe a base: "))
        alturaQ = float(input("Informe a altura: "))
        areaQ = calculodarea.areaquadrado(baseQ, alturaQ)
        print(f"A área do retângulo é {areaQ}")
    if tipo == 2:
        baseT = float(input("Informe a base: "))
        alturaT = float(input("Informe a altura: "))
        areaT = calculodarea.areatriangulo(baseT, alturaT)
        print(f"A área do triângulo é {areaT}")
    if tipo == 3:
        raio = float(input("Informe o raio: "))
        areaC = calculodarea.areacirculo(raio)
        print(f"A área do círculo é {areaC}")
