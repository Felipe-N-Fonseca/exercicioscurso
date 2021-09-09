# crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
# na ordem de colocação. depois mostre: apenas os 5 primeiros colocados, os ultimos 4 colocados,
# uma lista com nome em ordem alfabetica, em que posição na tabelaestá o time da chapecoense.

classificados = ('Atlético MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Atlético PR', 'Atlético GO',
                 'Ceará', 'Inter', 'Santos', 'Corinthians', 'Juventude', 'Bahia', 'São Paulo', 'Fluminense',
                 'Cuiabá', 'Sport Recife', 'América MG', 'Grêmio', 'Chape')

cha = 'Chape'

print('bem vindo a tabela do brasileirão:')
print('-=' * 100)
print('os times classificados são:')
print(classificados)
print('-=' * 100)
print('os 5 primeiros colocados são:')
print(classificados[0: 5])
print('-=' * 100)
print('os ultimos 4 são:')
print(classificados[-4: ])
print('-=' * 100)
print('em ordem alfabética:')
print(sorted(classificados))
print('-=' * 100)
print(f'e o chapecoense está em: {classificados.index(cha) + 1}')
