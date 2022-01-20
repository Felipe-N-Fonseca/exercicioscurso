# aprimore o exercicio 093 para que ele funcione com vários jogadores, incluindo um sistema de
# vizualização de detalhes do aproveitamento de cada jogador.

apr = {}
jogadores = []
partidas = []
total = 0
para = 'm'
cort = 0
while para not in 'nN':
    apr['nome'] = input('nome: ').strip().capitalize()
    apr['pj'] = int(input('partidas jogadas: '))
    for c in range(1, apr['pj']+1):
        partidas.append(int(input(f'quantos gols ele fez na {c} partida: ')))
    apr['gols'] = partidas[:]
    partidas.clear()
    for d in apr['gols']:
        total += d
    apr['total'] = total
    total = 0
    jogadores.append(apr.copy())
    para = input('deseja continuar? [s/n]: ')
    while para not in 'sSnN':
        para = input('digite apenas S ou N por favor: ')
print('__'*40)
print(f'{"n°":<5}{"NOME":<20}{"GOLS":<20}{"TOTAL":<4}')
print('__'*40)
for e,g in enumerate(jogadores):
    print(f"{e + 1:<5}{g['nome']:<20}{str(g['gols']):<20}{g['total']:<4}")
while cort != 999:
    cort = int(input('quer ver a nota de qual jogador mais detalhadamente? [999 encerra]:\n'))
    if cort != 999:
        print('-='*40)
        print(f"o jogador {jogadores[cort-1]['nome']} jogou {jogadores[cort-1]['pj']} partidas")
        for f,g in enumerate(jogadores[cort-1]['gols']):
            print(f'na partida {f+1}, fez {g} gols')
        print(f'no total foram feitos {jogadores[cort-1]["total"]} gols no campeonato')
        print('-='*40)
