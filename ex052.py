# faça um programa que leia um numero inteiro e diga se ele é ou não um número primo
# divisiveis por 1 e por ele mesmo

num = int(input('digite um número: '))
s = 0

for c in range(1, num +1):
    if num % c == 0:
        print(f'\033[0;32m {c} ', end=' ')
        s += 1
    else:
        print(f'\033[0;31m {c}', end=' ')

if s == 2:
    print('\033[0;32m ele é um número primo')
else:
    print('ele não é um número primo')
