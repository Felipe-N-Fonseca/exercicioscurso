# desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritimética
# e mostre os 10 primeiros termos dessa progressão aritimética

ter = int(input('digite o primeiro termo: '))
raz = int(input('digite a razão: '))
s = 0

for c in range(0, 10):
    print(f'{ter}' , end=' -> ')
    ter += raz
