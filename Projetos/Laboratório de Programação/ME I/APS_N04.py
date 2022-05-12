# Grupo:
# Christian Adriel de Santana Almeida
# Natalia Santos Oliveira
# Victor Gabriel Soares
# Felipe Matheus da Silva Mota
# Thales Ivan Silva Santos
# Rômulo Souza Silva


import funcoes


# Gerador de arquivos necessários
funcoes.gerador_arquivo_vagasReservadas()
funcoes.gerador_arquivo('Backup.txt')
funcoes.gerador_arquivo('Vagas.txt')
funcoes.gerador_arquivo('Exclusoes.txt')

# Variaveis necessárias
FILAS = 6
COLUNAS = 10
lugares = funcoes.arquivo_matriz_lugares()
clientes = {}
cpfs = {}
cliente = 'Backup.txt'
vaga = 'Vagas.txt'
relatorioExcluir = 'Exclusoes.txt'

# Função do cadastro
def cadastroVaga(cpf):
    with open('Backup.txt') as f:
        for x in f:
            if cpf in x:
                reserva_fila = int(input('Fila: '))
                assert 1 <= reserva_fila <= FILAS
                reserva_coluna = int(input('Coluna: '))
                assert 1 <= reserva_coluna <= COLUNAS
                if funcoes.consulta_reserva_vaga(lugares, reserva_fila, reserva_coluna):
                    print('Essa vaga já está reservada!')
                else:
                    funcoes.cadastrarVaga(vaga, cpf, reserva_fila, reserva_coluna)
                    lugares2 = funcoes.reserva_vaga(lugares, reserva_fila, reserva_coluna)
                    print(f'Vaga [{reserva_fila}][{reserva_coluna}] reservada para o cliente!')
                    funcoes.estacionamento(lugares2)
                break


# Programa
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
    print('7 - Vagas excluídas')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    
    if opcao == 1:
        funcoes.lerArquivo(vaga)
        
    elif opcao == 2:
        try:
            cpf = input('CPF do Cliente: ')
            cadastroVaga(cpf)
            funcoes.estacionamento(lugares)
        except AssertionError:
            print('Informação inválida')
            
    elif opcao == 3:
        funcoes.listar_vagas_disponiveis(lugares)
        
    elif opcao == 4:
        cpf = input('CPF da vaga que deseja apagar: ')
        funcoes.apagarReserva(cpf)
        reserva_fila = int(input('Fila: '))
        assert 1 <= reserva_fila <= FILAS
        reserva_coluna = int(input('Coluna: '))
        assert 1 <= reserva_coluna <= COLUNAS
        if funcoes.consulta_reserva_vaga(lugares, reserva_fila, reserva_coluna) == False:
            print('Essa vaga já está disponível!')
        else:
            lugares = funcoes.excluir_reserva(lugares, reserva_fila, reserva_coluna)
            print(f'Reserva da vaga [{reserva_fila}][{reserva_coluna}] excluída!')
            funcoes.cadastrarVaga(relatorioExcluir, cpf, reserva_fila, reserva_coluna)
            
    elif opcao == 5:
        nome = input('Nome do Cliente: ')
        funcoes.cadastrar_cliente(clientes, nome)
        cpf = int(input('Informe o CPF do Cliente: '))
        funcoes.cadastrar_cpf(cpfs, cpf)
        funcoes.cadastrarCliente(cliente, nome, cpf)
        
    elif opcao == 6:
        cpf = input('CPF do Cliente: ')
        funcoes.verificarVaga(cpf)
        
    elif opcao == 7:
        funcoes.lerArquivo(relatorioExcluir)
        
    elif opcao == 0:
        funcoes.estacionamento(lugares)
        print('Obrigado por usar esse programa!')
        
    elif opcao != 0:
        print('\n{0} não é uma opção valida'.format(opcao))

    print()