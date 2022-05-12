# criar uma tupla com tabela do brasileirão que mostre os 5 primeiros colocados, os 4 últimos, ordem alfabética e posição do chapecoense

tabela = ('Atlético', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Fluminense', 'Cuiabá', 'Internacional', 'Chapecoense')
cont = 0

print('--'*20)
print(f"Os 5 primeiros colocados da tabela são: ")
for c, i in enumerate(tabela[:5]):
    print(f"{c+1}º {tabela[c]}")
print('--'*20)

print(f"Os 4 últimos colocados da tabela são: ")
for k, j in enumerate(tabela[-4:]):
    print(f"{len(tabela)+cont}º {tabela[k]}")
    cont -= 1
print('--'*20)

print(f"A ordem alfabética da tabela é:")
print(sorted(tabela))
print('--'*20)

print(f"A posição do Chapecoense na tabela é: "
      f"{tabela.index('Chapecoense')+1}{'º'}")
print('--'*20)
