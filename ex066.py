# crie um programa que leia varios números inteiros, o programa só deve parar quando o usúario digitar 999,
# que é a condição de parada. no final mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag

soma = 0
vezes = 0

while True:
    n = int(input('digite um número (999 pra parar): '))
    if n == 999:
        break
    soma += n
    vezes += 1
print(f'a quantidade de números digitados foi de {vezes}')
print(f'a soma dos números foi {soma}')
