# crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. no final mostre:
# quantas pessoas foram cadastradas
# a média de idade do grupo
# uma lista com todas as mulheres.
# uma lista com todas as pessoas com idade acima da média

pessoas = {}
lista = []
soma = 0
para = 's'
mulheres = []
idadeacima = []
while para not in 'Nn':
    pessoas["nome"] = input('nome: ').strip().capitalize()
    pessoas["sexo"] = input('sexo [m/f]: ').strip().lower()
    while pessoas["sexo"] not in "MmFf":
        pessoas["sexo"] = input('digite apenas M ou F por favor: ')
    pessoas["idade"] = int(input('idade: '))
    lista.append(pessoas.copy())
    para = input('deseja continuar? [s/n]: ')
print('-='*40)
print(f'ao todo foram cadastradas {len(lista)} pessoas')
for c in range(0, len(lista)):
    soma += lista[c]["idade"]
    if lista[c]["sexo"] in 'f':
        mulheres.append(lista[c]["nome"])
soma /= len(lista)
for d in range(0, len(lista)):
    if lista[d]["idade"] > soma:
        idadeacima.append(lista[d]["nome"])
print(f'a média de idade é de {soma} anos')
if 1 == len(mulheres):
    print(f'o nome da unica mulher é {mulheres[0]}')
elif len(mulheres)  > 1:
    print(f'o nome das mulheres é {mulheres}')
else:
    print('não tem mulheres no grupo')
if 1 == len(idadeacima):
    print(f'{idadeacima[0]} é a pessoa com idade acima da média')
elif len(mulheres) > 1:
    print(f'as pessoas com idade acima da média são: {idadeacima}')
else:
    print('não tem pessoas acima da média de idade no grupo')

print('-='*40)
