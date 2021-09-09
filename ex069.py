# crie um programa que leia a idade e o sexo de varias pessoas. a cada pessoa cadastrada o
# programa deverá perguntar se o usuario quer ou não continuar, mostrando:
# quantas pessoas tem mais de 18, quantos homens foram cadastrados, quantas mulheres tem menos de 20

print('-=' *30)
print('bem vindo a analise de cadastro I')
print('')

mais18 = 0
homens = 0
mulheres = 0
idade = 0
sexo = 'n'
continuar = 'l'

while True:

    continuar = 'l'
    sexo = 'n'

    print('-=' * 30)
    print('')
    print('cadastre uma pessoa')
    print('')
    print('-=' * 30)
    print('')
    idade = int(input('digite a idade: '))
    while sexo not in 'mf':
        sexo = str(input('digite o sexo [m/f]: ')).strip().lower()
    print('')

    if idade > 17:
        mais18 += 1
    if sexo == 'm':
        homens += 1
    if idade <= 20 and sexo == 'f':
        mulheres += 1

    while continuar not in 'sn':
        continuar = str(input('deseja continuar? [s/n]: ')).strip().lower()

    if continuar == 'n':
        break

print(f'o número de pessoas com mais de 18 é {mais18}')
print(f'o número de homens foi de {homens}')
print(f'o número de mulheres com menos de 20 é de {mulheres}')
