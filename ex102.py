# crie um programa que tenha uma função fatorial() que receba dois parâmetros: o número a calcular e o
# outro chamado show, que será um valor lógico(opicional) indicando se será mostrado ou não na tela o
# processo de calculo fatorial, adicione também um doc

def fatorial(num, show=False):
    """
    calcula o fatorial de um número
    :param num: valor que será fatorado
    :param show: (opicional) mostra ou não o calculo da fatoração
    :return: resultado da fatoração de um número
    """
    fato = 1
    if show == True:
        for c in range(num,0,-1):
            fato *= c
            if c == 1:
                print(c, end=f' = {fato}')
            else:
                print(c, end=' * ')
    else:
        for c in range(num,0,-1):
            fato *= c
        print(fato)


fatorial(7,True)
help(fatorial)
