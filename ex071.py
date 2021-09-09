# crie um programa que simule o funcionamento de um caixa eletronico, no inicio pergunte ao usuario
# qual o valor que será sacado (número inteiro) e o programa deverá informar quantas cédulas de cada
# valor serão entregues, considerando que o caixa possui cedulas de 50, 20, 10 e 1

print('_' * 40)
print('bem vindo ao caixa eletronico')
print('_' * 40)
print('')

print('~~' * 20)
saque = int(input('quanto quer sacar: '))
print('~~' * 20)

print(f'as notas entregues para o valor de {saque} são de:')

valor = saque // 50

print(f'50 = {valor}')

resto = saque % 50
valor =  resto // 20

print(f'20 = {valor}')

resto = resto % 20
valor =  resto // 10

print(f'10 = {valor}')

resto = resto % 10
valor =  resto // 1

print(f'1 = {valor}')
print('~~' * 20)
