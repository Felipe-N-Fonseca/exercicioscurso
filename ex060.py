# faça um programa que leia um número e mostre seu fatorial
# ex: 5! = 5*4*3*2*1 = 120

num = int(input('digite um número: '))
conta = 1

while num > 0:

    conta *= num

    if num > 1:
        print(num, end= ' * ')
    else:
        print(f'{num} = {conta}')

    num -= 1
