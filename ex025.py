# crie um programa que leia o nome da pessoa e diga se nele tem ou não silva no nome

nome = str(input('digite seu nome: ')).strip()
nome = nome.lower()

n = 'silva' in nome

if n == True:
    print('seu nome possui Silva nele')
else:
    print('seu nome não poissui Silva nele')

