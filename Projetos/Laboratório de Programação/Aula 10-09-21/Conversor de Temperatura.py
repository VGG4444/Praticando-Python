# conversor de tipo que pede duas temperaturas e informa qual a mais alta, convertendo se necessário

import tempf

temp1c = False
temp1f = False
temp2c = False
temp2f = False

print("Bem vindo ao conversor de tipo!\n"
      "Digite 0 para tipo em Celsius"
      "Digite 1 para tipo em Fahrenheit")
while True:
    tipo1 = int(input("Informe o tipo da primeira temperatura: temperatura (0 ou 1): "))
    if tipo1 == 1:
        temp1c = True
    elif tipo1 == 2:
        temp1f = True
    else:
        print("Resposta inválida, tente novamente!")
        break
    tipo2 = int(input("Informe o tipo da segunda temperatura: temperatura (0 ou 1): "))
    if tipo2 == 1:
        temp2c = True
    elif tipo2 == 2:
        temp2f = True
    else:
        print("Resposta inválida, tente novamente!")
        break

    temperatura1 = int(input("Qual a primeira temperatura? "))
    temperatura2 = int(input("Qual a segunda temperatura? "))
    if temp1c is True and temp2c is True:
        if temperatura1 > temperatura2:
            print(f"A primeira temperatura ({temperatura1}°C) é maior!")
        elif temperatura2 > temperatura1:
            print(f"A segunda temperatura ({temperatura2}°C) é maior!")
        else:
            print(f"{temperatura1}°C e {temperatura2}°C são iguais!")
    elif temp1f is True and temp2f is True:
        if temperatura1 > temperatura2:
            print(f"A primeira temperatura ({temperatura1}°F) é maior!")
        elif temperatura2 > temperatura1:
            print(f"A segunda temperatura ({temperatura2}°F) é maior!")
        else:
            print(f"{temperatura1}°F e {temperatura2}°F são iguais!")
    elif temp1f is True:
        temperaturaC = tempf.tempc(temperatura1)
        if temperaturaC > temperatura2:
            print(f"{temperaturaC}°C é maior que {temperatura2}°F")


