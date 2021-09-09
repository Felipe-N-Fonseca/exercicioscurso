# crie um programa que leia o ano de nascimento de 7 pessoas e no final diga quantas ja são maiores
# de idade e quantas e quantas não são

from datetime import date

data = date.today().year

idade = 0

tempo = 0

maiores = 0

menores = 0

for c in range(0, 7):

    idade = int(input('digite o ano de nascimento: '))
    tempo = data - idade
    print(f'{tempo} anos')
    print('')

    if tempo >= 18:
        maiores += 1
    else:
        menores += 1

print('')
print(f'a quantidade de maiores de idade é de {maiores}')
print('')
print(f'a quantidade de menores de idade é de {menores}')

