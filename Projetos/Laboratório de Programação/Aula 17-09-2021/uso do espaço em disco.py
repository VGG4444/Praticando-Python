import saverelat
import btomb

while True:
    nome = str(input('Digite o nome do usuário: '))
    if nome == 'Sair':
        break
    espaco = float(input('Informe o espaço que ele ocupa em bytes: '))

    espacoC = btomb.btomb(espaco)

    saverelat.saver(nome, espacoC)
