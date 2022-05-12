# leia um número de 0 a 10 e mostre sua escrita por extenso

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

numero = 0

while True:
    numero = int(input("Digite um número de 0 a 10: "))
    if numero in range(0, 11):
        print(f"Seu número ({numero}) escrito por extenso fica: {extenso[numero]}")
    elif numero == -1:
        break
    else:
        numero = int(input("Número inválido, tente novamente! "))
        print(f"Seu número ({numero}) escrito por extenso fica: {extenso[numero]}")
