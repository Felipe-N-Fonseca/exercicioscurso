# desenvolva um programa que leia quatro valores e guarde em uma tupla, no final mostre:
# quantas vezes aparece o valor 9, em que posição foi digitado o primeiro 3
# quais foram os numeros pares

num = (int(input('digite um valor: ')), int(input('digite um valor: ')),
        int(input('digite um valor: ')), int(input('digite um valor: ')))

print(f'os valores digitados foram {num}')

print(f'o 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'o tres apareceu na posição: {num.index(3) + 1}')
else:
    print('o número 3 não foi digitado')

print('os valores pares são:')
for c in num:
    if c % 2 == 0:
        print(c)
