# faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e ultimo
# nomes separadamente

nome = str(input('digite seu nome')).strip()
nome = nome.title()
nome = nome.split()

qt = len(nome)

print(f'seu nome é {nome[0]}')
print(f'o seu sobrenome é {nome[qt - 1]}')
