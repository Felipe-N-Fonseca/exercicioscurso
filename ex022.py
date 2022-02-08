# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas
# o nome com todas minusculas
# quantas letras ao tod o sem considerar espaços
# quantas letras tem o primeiro nome

inteira = str(input('digite seu nome completo: ')).strip()

# o strip evita espaços inuteis

print(f'em maiusculas: {inteira.upper()}')
print(f'em minusculas: {inteira.lower()}')

li = inteira.split()

ct = len(li)

cont = len(li [1]) + len(li [2]) + len(li [0])

print(f'o nome tem {cont} letras')

pn = len(li [0])

print(f'o primeiro nome tem {pn} letras')

# felipe nascimento fonseca