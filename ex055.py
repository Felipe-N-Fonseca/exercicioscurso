# faça um programa que leia o peso de 5 pessoas e no final mostre qual foi o maior e o menor peso lidos

peso = 0
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'digite o peso da {c}° pessoa: '))

    if c == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'o menor peso foi de {menor}')
print(f'o maior peso foi de {maior}')
