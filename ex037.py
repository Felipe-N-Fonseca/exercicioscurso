# escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a conversão
# 1 para binario, 2 para octal 3 para hexadecimal

num = int(input('''digite um número:
'''))

op = int(input('''digite uma das opções de conversão:
[1] binário
[2] octal
[3] exadecimal
'''))

if op == 1:
    print(f'a conversão de {num} para binário é de {bin(num)[2:]}')
elif op == 2:
    print(f'a conversão de {num} para octal é de {oct(num)[2:]}')
elif op == 3:
    print(f'a conversão de {num} para hexadecimal é de {hex(num)[2:]}')
else:
    print('ops parece que você não escolheu uma opção válida, digite novamente.')

