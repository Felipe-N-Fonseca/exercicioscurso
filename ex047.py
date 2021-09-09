# crie um programa que mostre na tela todos os números pares entre 1 e 50.

for c in range(1, 51):
    d = c % 2
    if d == 0:
        print(c)
