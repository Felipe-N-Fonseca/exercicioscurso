# dentro do pacote utilidadesCeV que foi criado no exercicio 111, temos um módulo chamado dado.
# crie uma função chamada leiadinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadesCeV.moeda import resumo
from utilidadesCeV.dado import leiadinheiro

resumo(leiadinheiro('digite um valor: R$'), 10, 70)
# print(moeda.metade(dado.leiadinheiro('digite um valor: R$')))
