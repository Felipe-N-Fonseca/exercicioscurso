# melhore o ex028 só que agora o jogador vai tentar advinhar até acerar mostrando no fim quantas
# vezes foram nescessarias para que a pessoa acertasse

import random
from time import sleep

print('-=-' * 20)
num = int(input('tente adivinhar em que numero eu pensei: '))
print('-=-' * 20)
pc = random.randint(0, 10)
print('hummm...')
print('-=-' * 20)
sleep(2)

tentativas = 1
acerto = False

while not acerto:
    num = int(input('errou, tenta de novo: '))
    tentativas += 1
    if num == pc:
        acerto = True

print('aeeee acertou')
print(f'foram nescessárias {tentativas} vezes pra acertar')
