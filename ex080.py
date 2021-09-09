# crie um programa onde o usuario possa digitar cinco valores númericos e cadastre-os em uma lista,
# ja na posição correta de inserção (sem usar o sort()), no final mostre a lista ordenada na tela

lista = []
new = 0

for c in range(0, 5):
    new = int(input('digite um valor: '))

    if lista == []:
        lista.append(new)
    else:
        for n, t in enumerate(lista):
            if t > new:
                lista.insert(n , new)
                break
            elif lista[-1] < new:
                lista.append(new)


print(f'os valores na ordem são: {lista}')
# 46197
