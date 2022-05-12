def criacao_matriz(FILAS, COLUNAS):
    matriz = []
    for i in range(FILAS):
        linha = []
        for j in range(COLUNAS):
            linha.append(False)
        matriz.append(linha)
    return matriz


def impressao_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def consulta_reserva_vaga(matriz, filas, colunas):
    if matriz[filas-1][colunas-1]:
        return True
    else:
        return False


def reserva_vaga(matriz, filas, colunas):
    matriz[filas-1][colunas-1] = True
    return matriz


def listar_vagas_disponiveis(matriz):
    disponiveis = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == False:
                disponiveis.append(j+1)
        print(f'Fila {i+1}: {disponiveis}')
        disponiveis = []


def excluir_reserva(matriz, filas, colunas):
    matriz[filas-1][colunas-1] = False
    return matriz


def cadastrar_cliente(dic, nome):
    dic[nome] = '0'
    return dic


def consulta_reserva_cliente(dic, nome):
    return dic.get(nome)

def cadastrar_cpf(dic, cpfs):
    dic[cpfs] = '0'
    return dic


def consulta_reserva_cliente_cpf(dic, cpfs):
    return dic.get(cpfs)

def reserva_vaga_cliente(dic, nome, cpfs, filas, colunas):
    if dic.get(nome) == None:
        dic[nome] = 'Fila ' + filas + ' Coluna ' + colunas

    else:
        del dic[nome]
        dic[nome] = 'Fila ' + str(filas) + ' Coluna ' + str(colunas)

def estacionamento(matriz):
    with open('vagasReservadas.txt', 'w') as arquivo:
        linha = ''
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if j == len(matriz[i])-1:
                    arquivo.write(f'{matriz[i][j]}\n')
                else:
                    arquivo.write(f'{matriz[i][j]} - ')
                    
def gerador_arquivo_vagasReservadas():
    try:
        with open('vagasReservadas.txt', 'r') as arq:
            linha = arq.readlines()
    except FileNotFoundError:
        arquivo = open('vagasReservadas.txt', 'w')
        filas = 6
        colunas = 10
        lugares = criacao_matriz(filas, colunas)
        estacionamento(lugares)

        
def gerador_arquivo(arq):
    try:
        with open(arq, 'r') as arquivo:
            linha = arquivo.readlines()
    except FileNotFoundError:
        arquivo = open(arq, 'w')
        arquivo.close()
                               
def arquivo_matriz_lugares():
    matriz = []
    with open('vagasReservadas.txt', 'r') as arquivo:
        for l in arquivo:
            linhaArq = l.split(' - ')
            linhaMatriz = []
            for i in range(len(linhaArq)):
                linhaMatriz.append(eval(linhaArq[i]))
            matriz.append(linhaMatriz)
    return matriz


def verificarVaga(cpf):
    with open('Vagas.txt') as f:
        posicaoCPF = ""
        posicaoColuna = ""
        posicaoFila = ""
        posicaoNome = ""
        presente = 0
        for x in f:
            if cpf in x:
                dadoCadastro = x.split(';')
                posicaoCPF = dadoCadastro[0]
                posicaoFila = dadoCadastro[1]
                posicaoColuna = dadoCadastro[2]             
                presente = 1
        if presente == 1:
            print(f'O cliente com {posicaoCPF}, possui uma reserva '
                  f'na {posicaoFila}, {posicaoColuna}') 
        else:
            print('Cliente não cadastrado')

def cadastrarVaga(texto, nome, fila, coluna):
    try:
        texto = open(texto, 'at')
    except:
        print('Houve um erro!!')
    else:
        texto.write(f'CPF:{nome};FILA:{fila}; COLUNA:{coluna};\n')
        texto.close()

def cadastrarCliente(texto, nome, cpf):
    try:
        texto = open(texto, 'at')
    except:
        print('Houve um erro!!')
    else:
        texto.write(f'{nome}; CPF:{cpf};\n')
        print(f'Novo registro de {nome} adicionado. ')
        texto.close()
        
def lerArquivo(nome):
    texto = open(nome, 'rt')
    for linha in texto:
        dado = linha.split(';')
        print(f'{dado[0]:<30} {dado[1]:>6}Fila{dado[2]:>10}Coluna')

def apagarReserva(cpf):
    with open("Vagas.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if cpf not in line:
                f.write(line)
        f.truncate()
