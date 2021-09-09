# crie um programa onde o usuario digite uma expressão qualquer que use parenteses. seu aplicativo deverá
# analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

parenteses = 0
exp = str(input('digite uma expressão com parenteses: ')).strip()
for c, u in enumerate(exp):
    if u in '(':
        parenteses += 1
    elif u in ')':
        parenteses -= 1
if parenteses == 0:
    print('o número de parenteses esta correto')
elif parenteses > 0:
    print('esta faltando fechar um ou mais parenteses')
elif parenteses < 0:
    print('esta sobrando um ou mais parenteses')
