# adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que ja temos no modulo criado até aqui

import moedas

num = int(input('digite um valor: R$'))
moedas.resumo(num,10,70,True)
print(moedas.metade(num))
