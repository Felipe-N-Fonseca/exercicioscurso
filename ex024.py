# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "santo"

nome = str(input('digite o nome da sua cidade: ')).strip()

nome = nome.lower()

n = 'santo' in nome[:5]

if n == True:
    print('sua cidade começa com Santo')
else:
    print('sua cidade não começa com Santo')
