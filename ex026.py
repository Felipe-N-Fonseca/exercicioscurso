# faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "A"
# em qual posição ela aparece a primeira vez
# em qual posição ela aparece a ultima vez

frase = str(input('digite uma frase')).strip().lower()

ap = frase.find('a')
ap2 = frase.count('a')
ap3 = frase.rfind('a')

print(f'a letra "a" aparece {ap2} vezes')
print(f'ela aparece primeiro em {ap + 1} ')
print(f'ela aparece por ultimo em {ap3 + 1}')
