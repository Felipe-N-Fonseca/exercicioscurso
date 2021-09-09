# escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior, o segundo valor é maior ou não existe valor maior, os dois são iguais

num = float(input('digite um número: '))
on = float(input('digite outro número: '))

if num > on:
    print('o primeiro número é maior que o segundo')
elif num < on:
    print('o segundo número é maior que o primeiro')
else:
    print('os dois são iguais')
