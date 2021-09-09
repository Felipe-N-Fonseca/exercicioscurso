# escreva um programa que leia um número 'n' inteiro e mostre na tela os 'n' primeiros elementos
# de uma sequencia de fibonacci
# ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('digite quantos termos da sequencia de fibonacci você quer: '))

p = 0
o = 1
t = 0

print(p, end= ' -> ')
print(o, end= ' -> ')

while n != 2:
    t = p + o
    print(t, end= ' -> ')
    p = o
    o = t
    n -= 1
print('fim')
