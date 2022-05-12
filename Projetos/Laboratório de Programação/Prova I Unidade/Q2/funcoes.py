def cadastrarVeterinario(cfmv, nome, sexo):
    try:
        texto = open('Relatório_vet_ativo.txt', 'at')
    except:
        print('Houve um erro!!')
    else:
        texto.write(f'CFMV: {cfmv}; NOME: {nome}; SEXO: {sexo}; STATUS: ATIVO\n')
        print(f'O veterinário {nome} foi cadastrado. ')
        texto.close()


def cadastrar_veterinario_indisp(cfmv, nome, sexo):
    try:
        texto = open('Relatório_vet_inativo.txt', 'at')
    except:
        print('Houve um erro!!')
    else:
        texto.write(f'CFMV: {cfmv}; NOME: {nome}; SEXO: {sexo}; STATUS: INATIVO\n')
        print(f'O veterinário {nome} foi cadastrado. ')
        texto.close()


def cadastrarPets(texto, codRegistro, nome, especie):
    try:
        texto = open(texto, 'at')
    except:
        print('Houve um erro!!')
    else:
        texto.write(f'CODIGO DE REGISTRO: {codRegistro}; NOME: {nome}; ESPECIE: {especie}; \n')
        print(f'Cadastro de {nome} realizado com sucesso! ')
        texto.close()


def marcarConsulta(cfmv, codRegistro, data):
    with open('Relatório_vet_ativo.txt') as f:
        for x in f:
            if cfmv in x:
                with open('Relatório_pets.txt') as y:
                    for z in y:
                        if codRegistro in z:
                            texto = open('Consultas.txt', 'at')
                            texto.write(f'DATA: {data}; CFMV: {cfmv}; REGISTRO: {codRegistro}; \n')
                            print(f'Consulta marcada para o dia {data}. ')
                            texto.close()


def lerArquivo(nome):
    with open(nome, 'rt') as arquivo:
        x = arquivo.read()
    print(x)


def criarArquivo(nome):
    texto = open(nome, 'wt+')
    texto.close()


def cancelarConsulta(data, cfmv, codRegistro):
    with open("Consultas.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if data and cfmv and codRegistro not in line:
                f.write(line)
        f.truncate()
    print('A consulta foi desmarcada!')


def arquivoExiste(nome):
    try:
        texto = open(nome, 'rt')
        texto.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def gerador_arquivo(arq):
    try:
        with open(arq, 'r') as arquivo:
            linha = arquivo.readlines()
    except FileNotFoundError:
        arquivo = open(arq, 'w')
        arquivo.close()


def ganhoTotal(texto, ganhos):
        try:
            texto = open(texto, 'at')
        except:
            print('Houve um erro!!')
        else:
            texto.write(f'Os ganhos totais foram de R${ganhos} \n')
            texto.close()