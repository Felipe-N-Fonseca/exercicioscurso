# adapte o codigo do exercicio 107, criando uma função adicional chamada moeda() que consiga mostrar
# os valores como um valor monetário formatado.

import moedas

num = int(input('digite um valor: R$'))
print(f'a metade de {moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}')
print(f'o dobro de {moedas.moeda(num)} é {moedas.moeda(moedas.dobrar(num))}')
print(f'o aumento de {moedas.moeda(num)} em 10% é {moedas.moeda(moedas.aumentar(num, 10))}')
print(f'o desconto de {moedas.moeda(num)} em 50% é de {moedas.moeda(moedas.diminuir(num, 50))}')
