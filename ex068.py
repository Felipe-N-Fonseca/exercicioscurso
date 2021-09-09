# faça um programa que jogue par ou impar com o computador, o programa só para quando o jogador perder
# mostrando o total de vitórias consecultivas que ele teve

from random import randint

vitorias = 0
pi = 'n'

while True:

    pc = randint(0, 10)

    user = int(input('digite o número: '))
    while pi not in 'pi':
        pi = str(input('par ou impar? [p/i]: ')).strip().lower()

    pi = 'n'

    resultado = pc + user

    if pi  == 'p':
        if resultado % 2 == 0:
            vitorias += 1
        else:
            break
    else:
        if resultado % 2 == 1:
            vitorias += 1
        else:
            break

    print('aeee tu ganhou')

print('=-' * 20)
print(f'poxa perdeu')
print(f'o número de vitórias foi {vitorias}')
print('-=' * 20)
