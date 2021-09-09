# elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal
# e condição de pagamento
# a vista dinheiro ou cheque: 10% de desconto; a vista cartão: 5% desconto; 2x cartão: preço normal
# 3x ou mais: 20% de juros

preco = float(input('digite o valor do produto: '))
pagamento = str(input('qual a forma de pagamento?'
                      '\n dinheiro ou cartão: ')).strip().lower()

if pagamento == 'dinheiro':
    print(f'o valor a ser pago com desconto é de {preco - preco * 0.1}')
elif pagamento == 'cartão' or pagamento == 'cartao':
    vezes = int(input('em quantas vezes? '))
    if vezes == 1:
        print(f'o valor a ser pago com desconto é de {preco - preco * 0.05}')
    elif vezes == 2:
        print(f'o preço inteiro a ser pago é de {preco}')
    else:
        print(f'o valor inteiro a ser pago com juros é de {preco + preco * 0.2}')
else:
    print('digite uma opção valida')
