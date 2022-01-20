# aprimore o exercicio anterior, mostrando no final:
# a soma de todos os valores pares;
# a soma de todos os valores da terceira coluna
# o maior valor da segunda linha.

matriz = [[],[],[]]
par = ter = mai = 0
for c in range(0,3):
    for z in range(0,3):
        matriz[c].append(int(input(f'digite o valor da coordenada ({c+1}, {z+1}): ')))
print()
print('-='*40)
for d,e in enumerate(matriz):
    print(' '*25, end='')
    for f in range(0,3):
        print(f'[{e[f]:^3}]', end='')
        if e[f] % 2 == 0:
            par += e[f]
        if f == 2:
            ter += e[f]
        if d == 1 and e[f] > mai:
            mai = e[f]
    print()
print('-='*40)
print(f'a soma de todos os valores pares é {par}')
print(f'a soma dos valores da terceira coluna é {ter}')
print(f'o maior número da segunda coluna é {mai}')
