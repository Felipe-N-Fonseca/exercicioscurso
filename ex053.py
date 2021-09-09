# crie um programa que leia uma frase qualquer e diga se ela é um pálindromo desconsiderando os espaços
# palavras que lidas de tras pra frente são iguais de frente pra tras

pal = str(input('digite uma frase pra descobrir se ela é um pálindromo: ')).strip().lower()

print('')

print('pálindromos são palavras ou frases que invertidas formam a mesma palavra ou frase')

print('')

splitado = pal.split()
juntado = ''.join(splitado)
inverso = ''
for c in range(len(juntado) -1, -1, -1):
    inverso += juntado[c]

if inverso == juntado:
    print(f'e {pal} é um pálindromo')
else:
    print(f'e {pal} não é um pálindromo')
