# escreva um programa para aprovar o empresimo bancario para a compra de uma casa.
# o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario
# ou então o empréstimo será negado

print('\033[0;31m-=' * 20)
casa = float(input('\033[0;32mqual o valor da casa? '))
print('\033[0;31m-=' * 20)
print(' ')
print('\033[0;31m-=' * 20)
salario = float(input('\033[0;32mqual o seu salário? '))
print('\033[0;31m-=' * 20)
print(' ')
print('\033[0;31m-=' * 20)
prestacao = int(input('\033[0;32mem quantos anos pretende pagar? '))
print('\033[0;31m-=' * 20)
prestacoes = prestacao * 12
mensais = casa / prestacoes
print(' ')
print('\033[0;31m-=' * 20)
print(f'\033[0;32mo valor das prestações mensais é de R${mensais:.2f}')
if mensais > salario * 0.30:
    print('porém infelizemente exede o valor de 30% do seu salário e o empréstimo foi recusado')
else:
    print('seu empréstimo foi aprovado')
print('\033[0;31m-=' * 20)
