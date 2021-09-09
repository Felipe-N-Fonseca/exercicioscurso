# faça o computador pensar um numero entre 0 e 5 e eça pro usuario tentar descobrir o numero que
# o computador pensou. o programa devera escrever na tela se o usuario venceu ou não
import random

'''num = int(input('tente advinhar o numero que o computador pensou: '))
pc = random.randint(0, 5)

if num == pc:
    print('VOCÊ VENCEU PARABÉNS')
else:
    print('que pena você perdeu')

print(f'o numero que o pc pensou foi {pc}')
print(f'e o seu numero foi {num}')
'''
# ou

from time import sleep

print('-=-' * 20)
num = int(input('tente adivinhar em que numero eu pensei: '))
print('-=-' * 20)
pc = random.randint(0, 5)
print('hummm...')
print('-=-' * 20)
sleep(2)

if num == pc:
    print('PARABÉNS VOCÊ ACERTOU')
    print(f'nós dois pensamos em {pc}')
else:
    print('que pena vc errou')
    print(f'o numero que eu pensei foi {pc} e não {num}')
