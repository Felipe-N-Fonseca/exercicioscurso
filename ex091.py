# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# guarde esses resultados em um dicionário. no final, coloque esse dicionário em ordem, sabendo que o vencedor
# tirou o maior número no dado.

from random import randint
from operator import itemgetter
jogadores = {}
print('_'*33)
for c in range(1,5):
    jogadores[f'jogador{c}'] = randint(1,6)
for k,v in jogadores.items():
    print(f'o {k} tirou {v}')
organizado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('_'*33)
for c,d in enumerate(organizado):
    print(f'{c+1}° {d[0]} com {d[1]} pontos no dado')
print('_'*33)
