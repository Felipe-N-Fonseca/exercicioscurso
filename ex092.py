# crie um programa que leia um nome, ano de nascimento e carteira de trabalho e cadastreos(com idade)
# em um dicionario se por acaso a ctps for diferente de 0, o dicionário receberá também o ano de
# contratação e o salário. calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
dicionario = {}
dicionario['nome'] = input('nome: ')
dicionario['ano de nascimento'] = int(input('ano de nascimento: '))
dicionario['idade'] = date.today().year - dicionario['ano de nascimento']
dicionario['carteira de trabalho'] = int(input('digite o número da sua carteira de trabalho: '))
if dicionario['carteira de trabalho'] != 0:
    dicionario['ano de contratação'] = int(input('digite o ano de contratação: '))
    dicionario['salário'] = float(input('digite seu salário: '))
    dicionario['aposentadoria'] = (dicionario['ano de contratação'] + 35) - dicionario['ano de nascimento']
print('-='*33)
for k,v in dicionario.items():
    print(f'o {k} tem valor de {v}')
print('-='*33)
