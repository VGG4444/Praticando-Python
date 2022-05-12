#Grupo:
#Christian Adriel de Santana Almeida
#Natalia Santos Oliveira
#Victor Gabriel Soares
#Felipe Matheus da Silva Mota
#Thales Ivan Silva Santos
#Rômulo Souza Silva

import funcoes

#GERADOR DE ARQUIVOS
funcoes.gerador_arquivo('Relatório_vet_ativo.txt')
funcoes.gerador_arquivo('Relatório_vet_inativo.txt')
funcoes.gerador_arquivo('Consultas.txt')
funcoes.gerador_arquivo('Relatório_pets.txt')
funcoes.gerador_arquivo('Valor_Consulta.txt')
funcoes.gerador_arquivo('ganhoTotal.txt')

# PROGRAMA PRINCIPAL:
ganhos = 0
veterinarios_ativos = 'Relatório_vet_ativo.txt'
veterinarios_inativos = 'Relatório_vet_inativo.txt'
pets = 'Relatório_pets.txt'
consultas = 'Consultas.txt'
valor_consulta = 'Valor_Consulta.txt'
ganhoTotais = 'ganhoTotal.txt'


opcao = 1
while opcao != 0:
    print()
    print('=-' * 20)
    print('    Selecione a opção desejada:    ')
    print('    1 - Cadastrar veterinário')
    print('    2 - Cadastrar novo pet')
    print('    3 - Marcar consulta')
    print('    4 - Relatorio de Veterinários')
    print('    5 - Relatorio de Pets')
    print('    6 - Relatorio de Consultas')
    print('    7 - Cancelar consulta')
    print('    8 - Relátorio de ganhos totais')
    print('    0 - Sair')
    print('=-' * 20)
    print()
    opcao = int(input('Digite o número da opção desejada: '))
    if opcao == 1:
        cfmv = input('Digite o número CFMV do profissional: ')
        nome = str(input('Digite o nome do veterinário: '))
        sexo = str(input('Sexo [M/F]: ')).upper()
        status = str(input('Status do profissional [Ativo(1) / Inativo(2)]: '))
        if status == '1':
            funcoes.cadastrarVeterinario(cfmv, nome, sexo)
        elif status == '2':
            funcoes.cadastrar_veterinario_indisp(cfmv, nome, sexo)
        else:
            print('Você não selecionou uma opção válida.')
            
    elif opcao == 2:
        codRegistro = input('Digite o código de registro do pet: ')
        nome = str(input('Dgite o nome do pet: '))
        especie = str(input('Selecione a espécie do pet (Cão / Gato / Pássaro): ')).upper()
        funcoes.cadastrarPets(pets, codRegistro, nome, especie)
        
    elif opcao == 3:
        data = input('Informe a data para consulta (__/__/____): ')
        cfmv = input('Digite o cfmv do veterinário: ')
        cfmvPresente = 0
        codRegistroPresente = 0
        with open('Relatório_vet_ativo.txt', 'r') as arquivo:
            buscaVet = arquivo.readlines()
            for linha in buscaVet:
                if cfmv in linha:
                    cfmvPresente += 1
                    break
                else:
                    print('O veterinário não está ativo!')      
        if cfmvPresente == 1:
            codRegistro = input('Informe o número de registro do pet: ')
            with open('Relatório_pets.txt', 'r') as arq:
                buscaPets = arq.readlines()
                for linha in buscaPets:
                    if codRegistro in linha:
                        codRegistroPresente += 1
                        break
                    elif codRegistro not in linha:
                        print('O pet não está cadastrado!')
        else:
            print('Ocorreu um erro. :c')
        if codRegistroPresente == 1:
            print('Digite o número equivalente a espécie do seu animal:')
            print('1 - CÃO')
            print('2 - GATO')
            print('3 - PÁSSARO')
            especie2 = int(input('Digite o número: '))
            if especie2 == 1:
                ganhos += 100
                funcoes.marcarConsulta(cfmv, codRegistro, data)
                
            elif especie2 == 2:
                ganhos += 120
                funcoes.marcarConsulta(cfmv, codRegistro, data)

            elif especie2 == 3:
                ganhos += 150
                funcoes.marcarConsulta(cfmv, codRegistro, data)
            else:
                print('Você não digitou uma opção válida.')
        else:
            print('Ocorreu um erro. :c')
        
    elif opcao == 4:
        print('Os veterinários ativos são:')
        funcoes.lerArquivo(veterinarios_ativos)
        print('Os veterinários inativos são:')
        funcoes.lerArquivo(veterinarios_inativos)
        
    elif opcao == 5:
        funcoes.lerArquivo(pets)
        
    elif opcao == 6:
        funcoes.lerArquivo(consultas)
        print(f'O ganho total de hoje foi R${ganhos}.')

    elif opcao == 7:
        data = input('Informe a data da consulta: ')
        cfmv = input('Informe o CFMV do profissional: ')
        codRegistro = input('Digite o número de registro do pet: ')
        funcoes.cancelarConsulta(data, cfmv, codRegistro)
    
    elif opcao == 8:
        funcoes.lerArquivo(ganhoTotais)
        
    elif opcao == 0:
        print('Obrigado por usar o programa!')
        funcoes.ganhoTotal(ganhoTotais,ganhos)
        break
        