# faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores
# inteiros. seu programa tem que analisar todos os valores e dizer qual deles é maior.

def maior(*num):
    if len(num) == 0:
        print('-=' * 40)
        print('não foi passado nenhum valor')
        print('não existe maior')
    else:
        num = sorted(num, reverse=True)
        if num[0] == 0:
            print('-='*40)
            print('não foi passado nenhum valor')
            print('não existe maior')
        elif len(num) > 1:
            print('-=' * 40)
            print(f'foram informados {len(num)} números, sendo eles: ', end='')
            for c in num:
                print(c, end=' ')
            print()
            print(f'o maior foi {num[0]}')
        else:
            print('-=' * 40)
            print(f'foi informado 1 número, sendo ele: ', end='')
            for c in num:
                print(c, end=' ')
            print()
            print(f'o maior foi {num[0]}')


maior(1,2,3,4,5,6,7,8,9)
maior(52,2,57,2,7,4)
maior(4)
maior(0)
maior()
