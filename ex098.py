# faça um programa que tenha uma função chamada contador(), que receba três parametros:
# início, fim e passo e realize a contagem
# seu programa tem que realizar tres contagens através da função criada:
# de 1 até 10, de 1 em 1
# de 10 até 0 de 2 em 2
# uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c}, ', end='')
            sleep(0.3)
            c += passo
    else:
        c = inicio
        while c >= fim:
            print(f'{c}, ', end='')
            sleep(0.3)
            c -= passo
    print('FIM')


contador(0,10,1)
contador(10,0,2)
print('-='*20)
contador(int(input('digite o início: ')), int(input('digite o fim: ')), int(input('digite o passo: ')))
