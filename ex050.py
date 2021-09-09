# desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares
# desconsiderando os impares

s = 0

for c in range(1,7):
    n = int(input('digite um número: '))
    if n % 2 == 0:
        s += n
print(f'a soma dos números pares entre eles é de {s}')
