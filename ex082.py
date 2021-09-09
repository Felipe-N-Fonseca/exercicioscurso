# crie um programa que vai ler vários números e colocar em uma lista. depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. ao final, mostre
# o conteúdo das tres listas geradas

lista = []
pares = []
impares = []
while True:
    add = int(input('digite um número: '))
    lista.append(add)
    c = str(input('quer continuar?[s/n]: ')).strip().lower()
    if c in 'n':
        break
print(f'os números são {lista}')
for t, y in enumerate(lista):
    if y%2==0:
        pares.append(y)
    else:
        impares.append(y)
print(f'os pares são {pares}')
print(f'os impares são {impares}')
