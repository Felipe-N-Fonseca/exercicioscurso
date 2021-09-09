# crie um programa onde o usuario possa digitar varios valores numericos e cadastre os em uma lista
# caso o numero ja exista la dentro, ele não será adicionado. no final serão exibidos todos os valores
# unicos digitados, em ordem crescente

confi = 's'
num = []
new = 0
cont = 0
while confi not in 'n':
    confi = 'j'
    new = int(input('digite um número: '))

    if num == []:
        num.append(new)

    for t, c in enumerate(num):
        if c == new:
            cont = 1
    if cont != 1:
        num.append(new)
    cont = 0

    while confi not in 'sn':
        confi = str(input('deseja continuar? [s/n]: ')).strip().lower()

print()
print('-=' * 40)
num.sort()
print('os números digitados na ordem são: ')
for e, r in enumerate(num):
    print(r, end='... ')
print()
print('-=' * 40)


# alternativas:
# usar not in dentro do if ao inves do for pra procurar o numero
# usar um if com break ao invés de whille not
