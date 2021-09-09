# crie um programa que leia o nome e o preço de varios produtos. o programa deverá perguntar se o usuario
# vai continuar no final, mostre: qual é o total gasto na compra, quantos produtos custam mais de 1000
# qual o nome do produto mais barato

continuar = 's'
total = 0
maisde1000 = 0
maisbarato = ''
valormaisbarato = 10000
sim = 0

print('-=' * 20)
print('bem vindo ao caixa automatico')
print('-=' * 20)

while True:
    produto = str(input('digite o nome do produto: ')).strip()
    preco = float(input('digite o preço: '))

    if sim == 0:
        maisbarato = produto
        valormaisbarato = preco
        sim = 1

    continuar = str(input('quer continuar [s/n]: ')).strip().lower()
    while continuar not in 'sn':
        continuar = str(input('quer continuar [s/n]: ')).strip().lower()

    if preco < valormaisbarato:
        valormaisbarato = preco
        maisbarato = produto

    if preco >= 1000:
        maisde1000 += 1

    total += preco

    print('-=' * 20)

    if continuar == 'n':
        break

print('-=' * 20)
print('')

print(f'total: R${total:.2f}')
print(f'produtos maiores de R$1000: {maisde1000}')
print(f'produto mais barato: {maisbarato}')
