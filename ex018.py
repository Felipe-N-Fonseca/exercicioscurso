# faça um programa que leia um angulo qualquer e mostre na tela um valor do seno cosseno e tangente

import math

ai = int(input('digite um angulo: '))

a = math.radians(ai)

# os modulos de sin, cos e tan precisam estar em radianos, por isso a transformação acima

s = math.sin(a)
c = math.cos(a)
t = math.tan(a)

print(f'seu angulo é {a:.2f}')
print(f'o seno é {s:.2f}')
print(f'o cosseno é {c:.2f}')
print(f'a tangente é {t:.2f}')
