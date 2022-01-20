# crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica
# que mantenha separados os valores pares e impares. no final mostre os valores pares e impares em ordem crescente

tudo = [[],[]]
for c in range(0, 7):
    val = int(input('digite um valor númerico:\n'))
    if val % 2 == 0:
        tudo[0].append(val)
    else:
        tudo[1].append(val)
tudo[0].sort()
tudo[1].sort()
print(f'os valores pares foram {tudo[0]}')
print(f'os valores impares foram {tudo[1]}')
print(f'todos os valores foram {tudo}')
