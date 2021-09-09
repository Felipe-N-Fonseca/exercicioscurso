# escreva um programa que leia a velocidade de um carro. se ela ultrapassar 80 km/h, mostre uma mensagem dizendo que
# ele foi multado. a multa vai custar R$ 7,00 por cada km acima do limite

km = int(input('qual a velocidade atual do seu carro? '))

if km <= 80:
    print('-=-' * 25)
    print('muito bem continue assim')
    print('-=-' * 25)
else:
    print('-=-' * 25)
    print('po meu desacelera esse carro')
    print('-=-' * 25)
    print('você foi multado por exesso de velocidade')
    print('-=-' * 25)
    print(f'sua multa é de R${(km - 80) * 7 :.2f}')
    print('-=-' * 25)
