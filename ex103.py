# faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
# o nome de um joagdor e quantos gols ele marcou.
# o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
# informado corretamente

def ficha(j = '<desconhecido>', g = 0):
    """
    diz quantos gols um jogador fez
    :param j: nome do jogador
    :param g: quantia de gols
    :return: quantos gols um jogador fez
    """
    if j.strip() == '':
        j = '<desconhecido>'
    print('-='*20)
    print(f'o jogador {j} fez {g} gols')
    print('-=' * 20)


j = str(input('nome: ')).strip()
g = str(input('quantos gols ele fez? ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(j,g)
