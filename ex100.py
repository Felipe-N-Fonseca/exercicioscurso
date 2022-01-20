# faça um programa que tenha uma lista chamada números e duas funçôes chamadas sorteia() e somaPar().
# a primeira função vai sortear 5 números e coloca-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.

from random import random

def sorteia(liste):
    for c in range(0,5):
        liste.append(int(random() * 11))


def somaPar(num):
    d = 0
    for c in num:
        if c % 2 == 0:
            d += c
    print(f'e somando todos os valores pares eu obtive {d}')


lista = []
sorteia(lista)
print(f'sorteando 5 valores eu obtive: {lista}')
somaPar(lista)
