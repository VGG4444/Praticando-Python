"""
Utilizando os conceitos de modularização, crie um sistema simples para controlar
as reservas de um estacionamento. O estacionamento em questão possui 6 filleiras
com 10 posições cada uma.

X X X X X X X X X X X X X X
X X X X X X X X X X X X X X
X X X X X X X X X X X X X X
X X X X X X X X X X X X X X
X X X X X X X X X X X X X X
X X X X X X X X X X X X X X

Na primeira vez que o programa é executado, todas as vagas estão livres. Mas à
medida que o usuário vai realizando as reservas, as vagas devem ser marcadas
para não ficarem disponíveis para outras reservas. Dessa forma, se alguém tentar
reservar uma vaga já reservada, o sistema não deve permitir.
O programa deverá ter um menu para que o usuário possa navegar entre as
opções abaixo:
• Cadastro de Cliente (Nome, CPF) (0,2)
• Consulta de Clientes (Pelo CPF) (0,2)
• Reserva de Vaga (Fileira, Vaga e CPF do Cliente) (0,3)
• Cancelamento de Reserva de Vaga (Pelo CPF do Cliente) (0,2)
• Relatório de Reservas (Vaga + Cliente que reservou) (0,2)
• Relatório de Vagas Livres (0,2)
• Relatório de Cancelamento de Reservas de Vagas (0,2)
Todos os dados utilizados no sistema devem ser armazenados em arquivos TXT,
de forma que, quando o programa for iniciado, o mesmo deve levar em consideração informações já salvas nos arquivos,
e da mesma forma, a cada vez
que houver alteração de dados, estes devem ser salvos no arquivo.
"""

import funcoes

FILAS = 6
COLUNAS = 10
lugares = funcoes.criacao_matriz(FILAS, COLUNAS)
clientes = {}
cpfs = {}


opcao = 1
while opcao != 0:
    print('Escolha uma opção do menu:')
    print()
    print('1 - Consultar reservas')
    print('2 - Cadastrar reserva para o cliente')
    print('3 - Listar vagas disponíveis')
    print('4 - Excluir reserva')
    print('5 - Cadastrar cliente')
    print('6 - Consultar reserva do cliente')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if opcao == 1:
        funcoes.impressao_matriz(lugares)
    elif opcao == 2:
        try:
            reserva_fila = int(input('Fila: '))
            assert 1 <= reserva_fila <= FILAS
            reserva_coluna = int(input('Coluna: '))
            assert 1 <= reserva_coluna <= COLUNAS

            if funcoes.consulta_reserva_vaga(lugares, reserva_fila, reserva_coluna):
                print('Essa vaga já está reservada!')
            else:
                nome = input('Nome do Cliente: ')
                reserva = funcoes.consulta_reserva_cliente(clientes, nome)
                if reserva is None:
                    print('Cliente não cadastrado!')
                else:
                    funcoes.reserva_vaga_cliente(clientes, nome, cpfs, reserva_fila, reserva_coluna)
                    lugares = funcoes.reserva_vaga(lugares, reserva_fila, reserva_coluna)
                    print(f'Vaga [{reserva_fila}][{reserva_coluna}] reservada para o cliente {nome}!')
        except AssertionError:
            print('Informação inválida')
    elif opcao == 3:
        funcoes.listar_vagas_disponiveis(lugares)
    elif opcao == 4:
        try:
            reserva_fila = int(input('Fila: '))
            assert 1 <= reserva_fila <= FILAS
            reserva_coluna = int(input('Coluna: '))
            assert 1 <= reserva_coluna <= COLUNAS

            if not funcoes.consulta_reserva_vaga(lugares, reserva_fila, reserva_coluna):
                print('Essa vaga já está disponível!')
            else:
                lugares = funcoes.excluir_reserva(lugares, reserva_fila, reserva_coluna)
                print(f'Reserva da vaga [{reserva_fila}][{reserva_coluna}] excluída!')
        except AssertionError:
            print('Informação inválida')
    elif opcao == 5:
        nome = input('Nome do Cliente: ')
        funcoes.cadastrar_cliente(clientes, nome)
        cpf = int(input('Informe o CPF do Cliente: '))
        funcoes.cadastrar_cpf(cpfs, cpf)
    elif opcao == 6:
        nome = input('Nome do Cliente: ')
        reserva = funcoes.consulta_reserva_cliente(clientes, nome)
        if reserva is None:
            print('Cliente não cadastrado!')
        else:
            if reserva != '0':
                print(f'Cliente: {nome} - Reserva: {reserva}')
            else:
                print('Cliente não possui reserva!')
    elif opcao != 0:
        print('\n{0} não é uma opção valida'.format(opcao))

    print()
