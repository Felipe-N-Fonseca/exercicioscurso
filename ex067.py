# faça um programa que mostre a tabuada de vários números um de cada vez, para cada valor digitado pelo usuario
# o programa será interrompido quando o número solicitado for negativo.

while True:
    print('_-' * 20)
    n = int(input('digite o numero da tabuada \ndigite negativo para encerrar: '))
    print('-_' * 20)

    if n < 0:
        break

    for c in range(1, 11):
        print(f'{n} * {c} = {n * c}')
    print('-_' * 20)
