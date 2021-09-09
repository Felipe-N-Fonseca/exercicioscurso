# crie um programa que leia varios números e só pare quando sair uma sequencia 999
# no final mostre quantos numeros foram digitados e qual a soma entre eles desconsiderando o 999

f = '5'
c = 0
v = 0

while f not in '999':

    q = int(input('digite um número: '))
    w = int(input('digite um número: '))
    e = int(input('digite um número: '))

    c += q + w + e

    q = str(q)
    w = str(w)
    e = str(e)

    f = q + w + e
    v += 3

c -= 999
print('aeeee acertou finalmente')


