# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas no final do programa mostre a media
# de idade do grupo qual o nome do homem mais velho do grupo quantas mulheres tem menos de 20

idade = 0
nome = ''
sexo = 0

somaid = 0
maisvelho = 0
nomemaisvelho = ''
quantasmuie = 0

for c in range(1, 5):
    nome = str(input(f'qual o nome da {c}° pessoa: ')).strip()
    sexo = int(input(f'qual o sexo da {c}° pessoa\n1 para masculino, 2 para feminino: '))
    idade = int(input(f'qual a idade da {c}° pessoa: '))
    print('')

    somaid += idade

    if sexo == 1 and idade > maisvelho:
        nomemaisvelho = nome
        maisvelho = idade

    if sexo == 2 and idade < 20:
        quantasmuie += 1

somaid = somaid / 4

print(f'a média de idade do grupo é de {somaid}')
print('')
print(f'o nome do homem mais velho é {nomemaisvelho}')
print('')
print(f'as mulheres com menos de 20 são {quantasmuie}')


