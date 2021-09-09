# crie um programa que tenha uma unica tupla com nomes de produtos e seus respectivos preços
# no final mostre uma linguagem de preços organizados em forma tabular

produtos = ('Dolar Estadunidense', 5.38, 'Euro', 6.30, 'Libra', 7.40, 'Rubro', 0.073, 'Iens', 0.049,
            'Pesos Mexicanos', 0.27, 'Pesos Argentinos', 0.055, 'Dolar Canadense', 4.25)

print('\033[0;38m_'*50)
print('')
print(f"\033[0;33m{'lista de moedas':^50}\033[0;38m")
print('_'*50)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<40}', end='')
    else:
        print(f'R${produtos[c]:>6.2f}')

print('_'*50)
