# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

a = input('nome aluno 1 ')
b = input('nome aluno 2 ')
c = input('nome aluno 3 ')
d = input('nome aluno 4 ')

al = f'{a} {b} {c} {d}'.split()
random.shuffle(al)

print(f'a ordem de apresentação é {al}.')

# poderia também ter sido usada "lista = [a , b , c , d]" ao invés de usar o split
