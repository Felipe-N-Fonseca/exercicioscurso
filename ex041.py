# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria de acordo com a idade
# até 9: mirim; até 14: infantil; até 19: junior; até 20: sênior; acima master

from datetime import date

ano = int(input('qual o ano em que você nasceu: '))

idade = date.today().year - ano

if idade <= 9 and idade > 0:
    print('você faz parte do grupo mirim')
elif idade > 9 and idade <= 14:
    print('você faz parte do grupo infantil')
elif idade > 14 and idade <= 19:
    print('você faz parte do grupo júnior')
elif idade == 20:
    print('você faz parte do grupo sênior')
elif idade > 20:
    print('você faz parte do grupo master')
else:
    print('você veio do futuro???')

