def cadastro(arq):
    linha()
    printf('CADASTRO DE PESSOAS')
    linha()
    dicionario = {'nome': input('nome: '), 'idade': leiaInt('idade: ')}
    try:
        a = open(arq, 'at')
    except:
        print('\033[0;31mERRO AO LER ARQUIVO\033[m')
    else:
        try:
            a.write(f"{dicionario['nome']}:{dicionario['idade']}\n")
        except:
            print('\033[0;31mHOUVE UM ERRO AO ESCREVER O ARQUIVO\033[m')
        else:
            linha()
            printf('arquivo adicionado com sucesso')


def leiaIntTab(msg):
    """
    le apenas valores inteiros, pedindo nova digitação caso outro valor seja digitado
    :param msg: mensagem que será exibida
    :return: um número inteiro
    """
    n = 0
    while True:
        try:
            num = int(input(msg))
            if not 4 > num > 0:
                print('\033[1;31m__' * 23)
                print('  ERRO!!! digite apenas os números da tabela')
                print('¬¬' * 23, '\033[m')
                continue
        except:
            print('\033[1;31m__' * 21)
            print('  ERRO!!! digite apenas números inteiros')
            print('¬¬' * 21, '\033[m')
        else:
            return num



def leiaInt(msg):
    """
    le apenas valores inteiros, pedindo nova digitação caso outro valor seja digitado
    :param msg: mensagem que será exibida
    :return: um número inteiro
    """
    n = 0
    while True:
        try:
            num = int(input(msg))
        except:
            print('\033[1;31m__' * 21)
            print('  ERRO!!! digite apenas números inteiros')
            print('¬¬' * 21, '\033[m')
        else:
            return num


def listar(arq):
    linha()
    print('\033[0;35m', end='')
    printf('PESSOAS CADASTRADAS')
    linha()
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO AO LER ARQUIVO')
    else:
        print('\033[0;35m', end='')
        for c in a:
            b = c.replace('\n', '').split(':')
            print(f"{b[0]:<30}{b[1]:>3} anos")


def printf(msg,tam=40):
    print(f'{msg:^{tam}}')


def linha(tam=40):
    print('\033[0;94m~\033[0;93m' * tam)


def menu(arq):
    opcao = 0
    while opcao != 3:
        linha()
        print(f"\033[0;93m{'MENU PRINCIPAL':^40}")
        linha()
        print('\033[0;91m1 - \033[0;32mpara cadastrar alguém')
        print('\033[0;91m2 - \033[0;32mpara mostrar todos numa lista')
        print('\033[0;91m3 - \033[0;32mpara encerrar')
        linha()
        opcao = leiaIntTab('\033[0;93msua escolha: ')
        if opcao == 1:
            cadastro(arq)
        elif opcao == 2:
            listar(arq)
        else:
            linha()
            printf('saindo do sistema...')
            linha()
            break


