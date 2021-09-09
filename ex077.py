# crie um programa que tenha uma tupla com varias palavras (não usar acentos), depois disso você deve
# mostrar para cada palavra quais são suas vogais.

palavras = ('abecedario', 'parabolica', 'fernando', 'gay', 'esmalte', 'pedra', 'arroz', 'picles', 'narcoticos')

for c in palavras:
    print(f'\nna palavra {c} temos: ', end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l,  end=' ')
