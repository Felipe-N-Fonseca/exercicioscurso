# faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. no final mostre:
# quantas pessoas foram cadastradas;
# uma listagem com as pessoas mais pesadas;
# uma listagem com as pessoas mais leves;

pessoas = list()
dados = list()
e = 's'
p = 1
ma = me = 0
pma = []
pme = list()
while e not in 'Nn':
    dados.append(str(input('nome: \n')))
    dados.append(float(input('peso: \n')))
    pessoas.append(dados[:])
    if p == 1:
        ma = me = dados[1]
        pma.append(dados[0])
        pme.append(dados[0])
        p += 1
    else:
        if dados[1] > ma:
            pma.clear()
            ma = dados[1]
            pma.append(dados[:][0])
        elif dados[1] < me:
            pme.clear()
            me = dados[1]
            pme.append(dados[:][0])
        elif dados[1] == ma:
            pma.append(dados[:][0])
        elif dados[1] == me:
            pme.append(dados[:][0])

    dados.clear()
    e = input('deseja continuar? [s/n]: \n')
print(f'foram cadastradas {len(pessoas)} pessoas')
print(f'o maior peso foi {ma}Kg e quem o teve foi:', end=' ')
for c in pma:
    if len(pma) == 1:
        print(c)
    else:
        if c == pma[0]:
            print(c, end='')
        elif c == pma[len(pma)-1]:
            print(f', {c}.', end='\n')
        else:
            print(f', {c}', end='')
print(f'o menor peso foi {me}Kg e quem o teve foi:', end=' ')
for c in pme:
    if len(pme) == 1:
        print(c)
    else:
        if c == pme[0]:
            print(c, end='')
        elif c == pme[len(pme) - 1]:
            print(f', {c}.', end='\n')
        else:
            print(f', {c}', end='')
