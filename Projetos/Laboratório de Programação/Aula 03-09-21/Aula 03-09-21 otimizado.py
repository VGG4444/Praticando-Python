def conversor(hora, numero):
    convertido = hora - 12
    if numero >= 12:
        tempo = "PM"
    else:
        tempo = "AM"
    return convertido, tempo


tipo = 0
while True:
    horario = int(input("Digite a hora: "))
    if horario == -1:
        break
    if horario > 23:
        print("Digite uma hora válida!")
        break
    minutos = int(input("Digite os minutos: "))
    if minutos > 59:
        print("Digite minutos válidos!")
        break
    novaHora = conversor(horario, tipo)
    if horario > 12:
        print(f"{novaHora[0]}:{minutos} {novaHora[1]}")
    else:
        print(f"{horario}:{minutos} {horario}")
