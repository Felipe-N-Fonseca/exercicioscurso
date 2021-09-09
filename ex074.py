# crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla,
# depois disso mostre a listagem de números gerados e também indique o maior e o menor valor que estão na tupla

from random import randint

num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(num)
print(max(num))
print(min(num))
