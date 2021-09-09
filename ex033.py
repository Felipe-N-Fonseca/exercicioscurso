# faça um programa que leia 3 numeros e mostre qual é o maior e qual o menor

a = int(input('digite um número: '))
b = int(input('digite outro número: '))
c = int(input('digite mais um número: '))

# menor

me = a
if b < c and b < a:
    me = b
if c < a and c < b:
    me = c

# maior

ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c

print(f'o maior número é {ma}')
print(f'o menor número é {me}')
