# crie um programa que gerencie o aproveitamento de um jogador de futebol.
# o programa vai ler o nome do jogador e quantas partidas ele jogou. depois disso vai ler quantos gols ele fez em
# cada partida. no final tudo isso será guardado em um dicionário, imcluindo o total de gols feitos
# durante o campeonato

apr = {}
partidas = []
total = 0
apr['nome'] = input('nome: ')
apr['pj'] = int(input('partidas jogadas: '))
for c in range(1, apr['pj']+1):
    partidas.append(int(input(f'quantos gols ele fez na {c} partida: ')))
apr['gols'] = partidas
for d in partidas:
    total += d
apr['total'] = total
print('-='*40)
print(apr)
print('-='*40)
for k,v in apr.items():
    print(f'o campo {k} tem o valor de {v}')
print('-='*40)
print(f"o jogador {apr['nome']} jogou {apr['pj']} partidas")
for f,g in enumerate(partidas):
    print(f'na partida {f+1}, fez {g} gols')
print(f'no total foram feitos {total} gols no campeonato')
print('-='*40)
