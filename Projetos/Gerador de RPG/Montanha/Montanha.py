# Importando Bibliotecas
from random import randint
import mountain

# Menu Inicial

print("Bem vindo ao gerador de hexágono da Montanha!\n"
      "O que você deseja fazer?\n"
      "Digite 0 para gerar um hexágono ou digite 1 para gerar um encontro")
escolha = int(input("0 ou 1?: "))

# Escolha de Hexágono
# Descrição do Hexágono

if escolha == 0:
    primeiro = randint(1, 6) - 1
    segundo = randint(1, 6) - 1
    terceiro = randint(1, 6) - 1
    quarto = randint(1, 6) - 1
    resultadoH = mountain.descricao(primeiro, segundo, terceiro, quarto)
    print("="*50)
    print(f"Descrição do Hexágono")
    print(f"-"*50)
    print(f"Paisagem:   {resultadoH[0]}\n"
          f"Sons:       {resultadoH[1]}\n"
          f"Odores:     {resultadoH[2]}\n"
          f"Condição:   {resultadoH[3]}")
    print("=" * 50)

    cenario = randint(1, 20)
    listaCenarios = [["1-2 Assentamento"],
                     ["3-6 Paisagem Mundana"],
                     ["7 Ruínas"],
                     ["8-10 Nada de especial"],
                     ["11 Monumento"],
                     ["12-15 Obstáculo"],
                     ["16-17 Local Estranho"],
                     ["18-19 Marco na Paisagem"],
                     ["20 Fortaleza"]]
    if 0 < cenario < 3:
        assentamentoR = mountain.assentamento()
        print(f"Tipo de Cenário:        {listaCenarios[0]}")
        print(f"-" * 50)
        print(f"Tipo de Assentamento:   {assentamentoR[0]}\n"
              f"Ocupante Predominante:  {assentamentoR[1]}\n"
              f"Ocupação:               {assentamentoR[2]}\n"
              f"Povo:                   {assentamentoR[3]}\n"
              f"Habitação:              {assentamentoR[4]}")
    if 2 < cenario < 7:
        print(f"Tipo de Cenário: {listaCenarios[1]}")
        print(f"-" * 50)
        paisagemR = mountain.paisagemmundana()
        print(paisagemR)
    if 6 < cenario < 8:
        print(f"Tipo de Cenário: {listaCenarios[2]}")
        print(f"-" * 50)
    if 7 < cenario < 11:
        print(f"Tipo de Cenário: {listaCenarios[3]}")
        print(f"-" * 50)
    if 10 < cenario < 12:
        print(f"Tipo de Cenário: {listaCenarios[4]}")
        print(f"-" * 50)
    if 11 < cenario < 16:
        print(f"Tipo de Cenário: {listaCenarios[5]}")
        print(f"-" * 50)
    if 15 < cenario < 18:
        print(f"Tipo de Cenário: {listaCenarios[6]}")
        print(f"-" * 50)
    if 17 < cenario < 20:
        print(f"Tipo de Cenário: {listaCenarios[7]}")
        print(f"-" * 50)
    if 19 < cenario < 21:
        print(f"Tipo de Cenário: {listaCenarios[8]}")
        print(f"-" * 50)
