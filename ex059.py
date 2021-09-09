# crie um programa que mostre dois valores e mostre um menu na tela :
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# seu programa devera realizar a operação selecionada

from random import randint

al1 = randint(1, 99)
al2 = randint(1, 99)

print(f'você recebeu os valores {al1} e {al2}, escolha o que deve acontecer')
menu = int(input('[1] somar \n[2] multiplicar\n[3] maior\n[4] novos números \n[5] sair do programa \nsua escolha: '))

while menu != 5:
    print('-=' * 40)
    if menu == 1:
        print(f' a soma de {al1} + {al2} = {al1 + al2}')
    elif menu == 2:
        print(f'a multiplicação de {al1} * {al2} = {al1 * al2}')
    elif menu == 3:
        if al1 > al2:
            print(f'entre {al1} e {al2} o maior é {al1}')
        else:
            print(f'entre {al1} e {al2} o maior é {al2}')
    elif menu == 4:
        al1 = randint(1, 99)
        al2 = randint(1, 99)

        print(f'você recebeu os valores {al1} e {al2}, escolha o que deve acontecer')
    else:
        print('digite um valor valido')

    print('-=' * 40)

    menu = int(
        input('[1] somar \n[2] multiplicar\n[3] maior\n[4] novos números \n[5] sair do programa \nsua escolha: '))

print('')
print('fim do programa')
