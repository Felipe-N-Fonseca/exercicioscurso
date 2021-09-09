# crie um programa que leia varios números inteiros e no final mostre ao usuario a média entre todos os números
# e qual foi o maior e o menor valores lidos, o programa deve perguntar se o usuario quer continuar digitando

resp = 's'
vezes = 1
num = int(input('digite um número inteiro: '))
maior = menor = num
nv = num

while resp not in 'n':
    num = int(input('digite um número inteiro: '))
    nv += num
    vezes += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resp = str(input('deseja continuar? [n/s]: ')).strip().lower()

media = nv // vezes

print(f'o maior valor foi {maior}')
print(f'o menor valor foi {menor}')
print(f'e a média foi {media}')
