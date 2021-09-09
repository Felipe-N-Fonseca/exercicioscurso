# crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
# ex: digite 6.127 e a parte inteira é 6, usando o math
from math import floor
n = float(input('digite um numero com número após o ponto: '))
m = floor(n)
print(f'o número é {m}')

# ou importa o trunc que faz a mesma coisa
# ou simplesmente trasnforme o numero em int
