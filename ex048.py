# faça um programa que faça a soma de todos os números impares que são multiplos de 3
# no intervalo de 1 até 500

s = 0

for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print(f'a soma de todos os valores impares multiplos de 3 de 1 até 500 é de {s}')
