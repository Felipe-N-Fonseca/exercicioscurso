# crie um programa que vai ler vários números e colocar em uma lista. depois disso, mostre:
# a) quantos números foram digitados. b) a lista de valores ordenada de forma decrescente
# c) se o valor 5 foi digitado e está ou não na lista

lista = []
cinco = False
while True:
    new = int(input('digite um número: '))
    if new == 5:
        cinco = True
    lista.append(new)
    v = str(input('quer continuar?[s/n]: ')).strip().lower()
    if v in 'n':
        break
lista.sort(reverse=True)
print(f'você digitou {len(lista)} números')
print(f'a lista de valores em ordem decressente é de:')
print(lista)
if cinco == True:
    print('o número 5 estava presente')
else:
    print('o número 5 não está presente')
