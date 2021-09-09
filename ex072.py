# crie uma tupla com contagem de 0 até 20 por extenso, seu programa deverá ler um número pelo teclado
# e mostralo por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    cont = 'l'
    teclado = int(input('digite um número de 0 à 20 para telo por extenso: '))
    while True:
        if teclado >= 0 and teclado <= 20:
            break
        teclado = int(input('digite um valor de 0 à 20: '))

    print(numeros[teclado])
    while cont not in 'sn':
        cont = str(input('quer continuar? [s/n]: ')).strip().lower()
    if cont == 'n':
        break
