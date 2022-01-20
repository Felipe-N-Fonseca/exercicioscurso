# crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante á função input()
# do python, só que fazendo a validação para receber apenas um valor númerico
# ex: n = leiaint('digite um número')

def leiaint(msg):
    """
    le apenas valores inteiros, pedindo nova digitação caso outro valor seja digitado
    :param msg: mensagem que será exibida
    :return: um número inteiro
    """
    num = input(msg)
    while not num.isnumeric():
        print('\033[1;31m__'*20)
        print('  ERRO!!! valor não numérico detectado')
        print('¬¬'*20,'\033[m')
        num = input('por favor digite apenas números: ')
    return num


print(f'você digitou o número {leiaint("digite um número: ")}')
