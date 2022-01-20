# crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# no fim mostre um boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada
# aluno individualmente.

lista = []
td = []
resp = 's'
cort = 0
while resp not in 'nN':
    td.append(input('digite o nome do aluno: '))
    td.append(float(input('digite a 1° nota do aluno: ')))
    td.append(float(input('digite a 2° nota do aluno: ')))
    lista.append(td[:])
    td.clear()
    resp = input('quer continuar? [s/n]: ')
print('__'*40)
print(f'{"n°":<5}{"NOME":<20}{"MÉDIA":<4}')
print('__'*40)
for c, d in enumerate(lista):
    print(f'{c+1:<5}{d[0]:<20}{((d[1]+d[2])/2):<4}')
print('__'*40)
while cort != 999:
    cort = int(input('quer ver a nota de qual aluno mais detalhadamente? [999 encerra]:\n'))
    if cort != 999:
        print(f'as notas de {lista[cort-1][0]} foram {lista[cort-1][1]} e {lista[cort-1][2]}')
        print('__'*40)
