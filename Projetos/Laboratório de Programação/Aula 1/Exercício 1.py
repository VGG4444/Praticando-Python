nome = 0
dias = 0
distancia = 0
placa = 0
clientes = 0
valorDia = 0
valorDistancia = 0
distanciaTotal = 0
mediaDistancia = 0
mulheres = []

while True:
    nome = input('Insira o nome do cliente: ')
    if nome == 'SAIR':
            break
    sexo = input('Insira o sexo do cliente (M ou F): ').capitalize()
    placa = input('Insira a placa do carro alugado: ')
    distancia = int(input('Insira a quantidade de kilômetros contratados: '))
    dias = int(input('Insira a quantidade de dias contratados: '))
    valorDia = dias * 70
    valorDistancia = distancia * 0.10
    valorTotal = valorDia + valorDistancia

    print(f'Placa do carro: {placa}.', f'Preço a se pagar: R${valorTotal}')
    clientes += 1
    distanciaTotal += distancia
    mediaDistancia = distanciaTotal / clientes
    if sexo == 'F' and dias < 7:
        mulheres.append(nome)


print(mediaDistancia)

print(valorDia)
print(valorDistancia)
