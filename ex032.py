# faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
num = int(input('digite um ano: '))

if num == 0:
    num = date.today().year

if num == 0 and num % 100 != 0 or num % 400 == 0:
    print(f'o ano de {num} é um ano bissexto')
else:
    print(f'o ano de {num} não é um ano bissexto')
