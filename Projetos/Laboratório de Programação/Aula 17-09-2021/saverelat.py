def saver(nome, espaco):
    with open('relatório.txt', 'a') as salvando:
        salvando.write(f"Nome: {nome}\n"
                       f"Espaco em disco: {espaco}MB\n"
                       f"\n")
