# modifique as funções que foram criadas no exercicio 107 para que elas aceitem um parametro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no 108

import moedas

num = int(input('digite um valor: R$'))
print(f'a metade de {moedas.moeda(num)} é {moedas.metade(num, True)}')
print(f'o dobro de {moedas.moeda(num)} é {moedas.dobrar(num, True)}')
print(f'o aumento de {moedas.moeda(num)} em 10% é {moedas.aumentar(num, 10, True)}')
print(f'o desconto de {moedas.moeda(num)} em 50% é de {moedas.diminuir(num, 50, True)}')
