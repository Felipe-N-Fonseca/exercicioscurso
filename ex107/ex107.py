# crie um módulo chamado moedas.py que tenha funções incorporadas:
# aumentar(), diminuir(), dobra() e metade()
# faça também um programa que importe esse módulo e use algumas dessas funções

import moedas

num = int(input('digite um valor: '))
print(f'a metade de R${num} é R${moedas.metade(num):.2f}')
print(f'o dobro de R${num} é R${moedas.dobrar(num):.2f}')
print(f'o aumento de R${num} em 10% é R${moedas.aumentar(num, 10):.2f}')
print(f'o desconto de R${num} em 50% é de R${moedas.diminuir(num, 50):.2f}')
