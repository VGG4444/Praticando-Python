#Grupo:
#Christian Adriel de Santana Almeida
#Natalia Santos Oliveira
#Victor Gabriel Soares
#Felipe Matheus da Silva Mota
#Thales Ivan Silva Santos
#Rômulo Souza Silva

import funcoes
# GERADOR DE ARQUIVOS:
funcoes.gerador_arquivo('Clientes.txt')
funcoes.gerador_arquivo('Maquinas_disponiveis.txt')
funcoes.gerador_arquivo('Maquinas_indisponiveis.txt')
funcoes.gerador_arquivo('Reservas.txt')


clienteArq = 'Clientes.txt'
maquinas_disp = 'Maquinas_disponiveis.txt'
maquinas_indisp = 'Maquinas_indisponiveis.txt'
reservas = 'Reservas.txt'

# PROGRAMA PRINCIPAL:
clientes = {}
cpfs = {}
maquinas = []
invalido = 'Você não selecionou uma opção válida.'

opcao = 1
while opcao != 0:
    print()
    print('=-' * 20)
    print('    Selecione a opção desejada:    ')
    print('    1 - Cadastrar máquina')
    print('    2 - Cadastrar cliente')
    print('    3 - Reservar máquina')
    print('    4 - Relatorio de clientes')
    print('    5 - Relatorio de maquinas')
    print('    6 - Relatorio de alugueis')
    print('    0 - Sair')
    print('=-' * 20)
    print()
    opcao = int(input(f'Digite o número da opção desejada: '))
    if opcao == 1:
        maquina = str(input(f'Digite o nome da máquina para cadastrar: '))
        maquinas.append(maquina)
        cadastro_Cod = input(f'Digite o código da máquina: ')
        marca = input(f'Digite a marca da máquina: ')
        modelo = input(f'Digite o modelo da máquina: ')
        ano = int(input(f'Digite o ano da máquina: '))
        valor = float(input(f'Digite o valor do aluguel: '))
        status = input(f'Determine o status da máquina [D/I]: ')
        if status == 'D':
            funcoes.cadastro_maquinas_disponiveis(maquina, cadastro_Cod, marca, modelo, ano, valor, status)
        elif status == 'I':
            funcoes.cadastro_maquinas_indisponiveis(maquina, cadastro_Cod, marca, modelo, ano, valor, status)
        else:
            print(invalido)
    elif opcao == 2:
        cliente = input('Digite o nome do cliente: ')
        funcoes.cadastrar_cliente(clientes, cliente)
        cpf = int(input(f'Informe o CPF do Cliente: '))
        funcoes.cadastrar_cpf(cpfs, cpf)
        funcoes.cadastrarCliente(cliente, cpf)
    elif opcao == 3:
        nome = input('Digite seu nome: ')
        cpf = input('CPF: ')
        codigo = input('Codigo da maquina: ')
        funcoes.cadastrarReserva(codigo, nome, cpf)
    elif opcao == 4:
        funcoes.lerArquivo(clienteArq)
    elif opcao == 5:
        funcoes.lerArquivo(maquinas_disp)
        funcoes.lerArquivo(maquinas_indisp)
    elif opcao == 6:
        funcoes.lerArquivo(reservas)
    elif opcao == 0:
        print('Obrigado por usar o programa!')
    else:
        print(invalido)