# faça um programa que ajude um jogador da mega sena a criar palpites. o programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 pra cada jogo, cadastrando
# tudo em uma lista composta.

from random import randint
sort = []
jogos = []
print('--'*40)
print(f'{"JOGOS DA MEGA SENA":^80}')
print('--'*40)
vezes = int(input('digite quantos jogos você quer que eu sorteie: '))
print('-=' * 40)
for c in range(0, vezes):
    d = 0
    while d != 6:
        sorteado = randint(1, 60)
        if sorteado not in sort:
            sort.append(sorteado)
            d += 1
    sort.sort()
    print(f'Jogo {c+1}: {sort}')
    jogos.append(sort[:])
    sort.clear()
print('-='*40)
