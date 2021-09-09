# faça um programa que faça a contagem regressiva até o estouro de um fogos, indo de 10 até 0
# com uma pausa de 1 segundo entre eles

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOOOM')
