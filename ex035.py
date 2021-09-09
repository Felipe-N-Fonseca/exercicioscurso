# desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem
# ou não formar um triangulo. essa ai tem que pesquisar a regra matematica

print('-=' *20)
print('bem vindo ao analisador de triangulos')
print('ele ira analisar se suas retas podem formar um triangulo')
print('-=' * 20)

s1 = float(input('digite um seguimento: '))
s2 = float(input('digite outro seguimento: '))
s3 = float(input('digite o ultimo seguimento: '))
print('-=' * 20)

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('esse triangulo pode existir')
else:
    print('esse triangulo não pode existir')
print('-=' * 20)
print('obrigado por usar o analisador')
