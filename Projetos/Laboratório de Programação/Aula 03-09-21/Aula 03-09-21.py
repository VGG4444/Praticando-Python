def conversor(hora):
    convertido = hora - 12
    return convertido


def ampm(numero):
    if numero >= 12:
        tempo = "PM"
    else:
        tempo = "AM"
    return tempo


while True:
    horario = int(input("Digite a hora: "))
    if horario == -1:
        break
    minutos = int(input("Digite os minutos: "))
    novaHora = conversor(horario)
    if horario > 12:
        print(f"{novaHora}:{minutos} {ampm(horario)}")
    else:
        print(f"{horario}:{minutos} {ampm(horario)}")
