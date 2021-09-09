# faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# se ele ainda vai se alistar no exercito, se é a hora de se alistar, se ja passou a data de alistamento
# seu programa também deve mostrar quanto tempo falta ou passou da data de alistamento

from datetime import date

idade = int(input('digite o ano que você nasceu: '))

data = date.today().year - idade

if data <= 17:
    print(f'ainda não chegou sua vez de se alistar, faltam {18 - data} anos pra você se alistar')
elif data == 18:
    print('aliste-se imediatamente')
else:
    print(f'sua data de alistamento ja passou, fazem {data - 18} anos')
