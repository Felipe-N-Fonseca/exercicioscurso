# reescreva a função leiaInt() que fizemos no desafio 104, incluindo a possibilidade da digitação de
# um número de tipo inválido. aproveite também e crie uma função leiaFloat() com a mesma funcionalidade

def leiaInt(msg):
    """
    le apenas valores inteiros, pedindo nova digitação caso outro valor seja digitado
    :param msg: mensagem que será exibida
    :return: um número inteiro
    """
    n = 0
    while n != 1:
        try:
            num = int(input(msg))
            n += 1
        except:
            print('\033[1;31m__' * 21)
            print('  ERRO!!! digite apenas números inteiros')
            print('¬¬' * 21, '\033[m')
        else:
            return num


def leiaFloat(msg):
    """
    le apenas valores númericos, pedindo nova digitação caso outro valor seja digitado
    :param msg: mensagem que será exibida
    :return: um número inteiro
    """
    n = 0
    while n != 1:
        try:
            num = float((input(msg)).replace(',','.'))
            n += 1
        except:
            print('\033[1;31m__' * 21)
            print(f"{'ERRO!!! digite apenas números':^42}")
            print('¬¬' * 21, '\033[m')
        else:
            return num


print(leiaInt('digite um número: '))
print(leiaFloat('digite um número: '))
