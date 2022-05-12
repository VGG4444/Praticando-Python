# ler a distancia de uma viagem e calcular o preço por 0,50 por km por viagens de até 200km e 0,45 por mais

preco = 0

distancia = int(input("Digite a distãncia da viagem: "))
if distancia <= 200:
    preco = distancia * 0.50
    print(f"Sua passagem tem valor de R${preco}")
else:
    preco = distancia * 0.45
    print(f"Sua passagem tem valor de R${preco} pois sua viagem foi mais longa!")
