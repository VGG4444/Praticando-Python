def cadastrar_cliente(dic, nome):
    dic[nome] = '0'
    return dic


def cadastro_maquinas_disponiveis(maquina, codigo, marca, modelo, ano, valor, status):
    try:
        arq = open('Maquinas_disponiveis.txt', 'at')
    except:
        print('Houve um erro!!')
    else:
        arq.write(f'Maquina: {maquina}; codigo: {codigo}; marca:{marca}; modelo:{modelo};ano:{ano}; valor:{valor}; status:{status}\n')
        print()
        print(f'Novo registro de {maquina} adicionado. ')
        arq.close()

def cadastro_maquinas_indisponiveis(maquina, codigo, marca, modelo, ano, valor, status):
    try:
        arq = open('Maquinas_indisponiveis.txt', 'at')
    except:
        print('Houve um erro!!')
    else:
        arq.write(f'Maquina: {maquina}  codigo: {codigo}    marca:{marca}   modelo:{modelo}   ano:{ano}    valor:{valor}    status:{status}\n')
        print()
        print(f'Novo registro de {maquina} adicionado. ')
        arq.close()

def consulta_reserva_cliente(dic, nome):
    return dic.get(nome)


def cadastrar_cpf(dic, cpfs):
    dic[cpfs] = '0'
    return dic


def consulta_reserva_cliente_cpf(dic, cpfs):
    return dic.get(cpfs)

def cadastrarCliente(nome, cpf):
    try:
        arq = open('Clientes.txt', 'at')
    except:
        print('Houve um erro!!')
    else:
        arq.write(f'NOME: {nome}; CPF: {cpf};\n')
        print()
        print(f'Novo registro de {nome} adicionado. ')
        arq.close()


def cadastrarReserva(identificador, nome, cpf):
    with open('Maquinas_disponiveis.txt') as f:
        maquina = ''
        marca = ''
        ano = ''
        status = 'I'
        valor = ''
        tipo = ''
        codigo = ''
        presente = 0
        for x in f:
            if identificador in x:
                dadoCadastro = x.split(';')
                maquina = dadoCadastro[0]
                codigo = dadoCadastro[1]
                marca = dadoCadastro[2]
                tipo = dadoCadastro[3]
                ano = dadoCadastro[4]
                valor = dadoCadastro[5]
                presente = 1
            if presente == 1 :
                texto = open('Reservas.txt', 'at')
                texto.write(f'NOME:{nome}; CPF:{cpf}; {codigo}; {tipo}; {valor}\n')
                texto.close()
                presente += 1
            if presente == 2:
                atualizar = open('Maquinas_indisponiveis.txt', 'at')
                atualizar.write(f'{maquina}; {codigo}; {marca}; {tipo}; {ano}; {valor}; {status}\n')
                atualizar.close()
                apagarReserva(codigo)


def lerArquivo(nome):
    with open(nome, 'rt') as arquivo:
        x = arquivo.read()
    print(x)

def arquivoExiste(nome):
    try:
        texto = open(nome, 'rt')
        texto.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    texto = open(nome, 'wt+')
    texto.close()

def apagarReserva(codigo):
    with open("Maquinas_disponiveis.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if codigo not in line:
                f.write(line)
        f.truncate()

def gerador_arquivo(arq):
    try:
        with open(arq, 'r') as arquivo:
            linha = arquivo.readlines()
    except FileNotFoundError:
        arquivo = open(arq, 'w')
        arquivo.close()