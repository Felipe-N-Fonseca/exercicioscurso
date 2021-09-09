# faça um programa que leia 5 valores e guarde os em uma lista, no final mostre qual foi o
# maior e qual foi o menor valor digitado e sua posição na lista

lista = []

for c in range(0,5):
    lista.append(int(input(f'digite o valor da posição {c}: ')))

print(f'os valores digitados foram {lista}')

aplicada = lista[:]
aplicada.sort()

mai = aplicada[4]
men = aplicada[0]

print(f'o maior numero digitado foi {mai} e apareceu nas posições: ' , end='')
for c, a in enumerate(lista):
    if a == mai:
        print(f' {c+1}...' , end='')
print()
print(f'o menor número digitado foi {men} e apareceu nas posições: ' , end='')
for c, a in enumerate(lista):
    if a == men:
        print(f' {c+1}...' , end='')
