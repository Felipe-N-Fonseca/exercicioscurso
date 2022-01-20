# crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# no final mostre a matriz na tela com a formatação correta.

matriz = [[],[],[]]
for c in range(0,3):
    for z in range(0,3):
        matriz[c].append(int(input(f'digite o valor da coordenada ({c+1}, {z+1}): ')))
print()
print('-='*40)
for d,e in enumerate(matriz):
    print(' '*25, end='')
    for f in range(0,3):
        print(f'[{e[f]:^3}]', end='')
    print()
print('-='*40)
