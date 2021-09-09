# crie um progra que leia um numero inteiro e mostre na tela se é par ou impar

num = int(input('digite um numero: '))
resto = num % 2

if resto == 1:
    print(f'{num} é um numero impar')
else:
    print(f'{num} é um numero par')
