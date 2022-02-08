def verificaArquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ops, tivemos um problema na criação do arquivo')
    else:
        print(f'o arquivo {nome} foi criado com sucesso')
