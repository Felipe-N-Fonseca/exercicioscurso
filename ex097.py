# faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parãmetro
# e mostre uma mensagem com tamanho adaptável
# ex: escreva(olá mundo)
# saída:
# ~~~~~~~~~~
# olá mundo!
# ~~~~~~~~~~

def escreva(text):
    print('~'*(len(text)+2))
    print(f" {text} ")
    print('~' * (len(text) + 2))


escreva(input('digite uma frase: '))
escreva(input('digite outra: '))
escreva(input('digite mais uma: '))
