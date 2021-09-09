# cire um programa que joga jokenpô com você

from random import randint
from time import sleep

passe = randint(1, 3)

if passe == 1:
    jk = 'pedra'
elif passe == 2:
    jk = 'papel'
else:
    jk = 'tesoura'

print('vamos jogar pedra papel e tesoura?')

player = (str(input('vamos lá digite qual seu movimento '
                    '\n pedra, papel ou tesoura apenas viu: '))).strip().lower()

if player == 'pedra' or player == 'tesoura' or player == 'papel':
    sleep(1)
    print('pedraaa')
    sleep(1)
    print('papel')
    sleep(1)
    print('tesou...ra')
    sleep(1)

    print()

    if jk == 'pedra' and player == 'tesoura':
        print('ahh eu ganhei')
    elif jk == 'papel' and player == 'pedra':
        print('ahaaaa eu ganhei')
    elif jk == 'tesoura' and player == 'papel':
        print('ihaaa eu ganhei')
    elif jk == 'pedra' and player == 'papel':
        print('opa tu ganhou... grrrrr')
    elif jk == 'papel' and player == 'tesoura':
        print('ops você ganhou... ahhhh')
    elif jk == 'tesoura' and player == 'pedra':
        print('oh merda perdi')
    else:
        print('parece que empatamos né')

    print()

    print(f'você escolheu {player} e eu escohi {jk}')
else:
    print('digite um valor valido')

