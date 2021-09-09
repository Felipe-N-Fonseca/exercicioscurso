# refaça o ex051 usando o wille

termo = int(input('digite o termo: '))
razao = int(input('digite a razão: '))
s = 10

while s > 0:
    if s > 1:
        print(termo, end= ' -> ')
    else:
        print(termo)
    termo += razao
    s -= 1
