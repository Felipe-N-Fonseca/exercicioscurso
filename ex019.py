# um professor quer sortear um de seus 4 alunos pra apagar o quadro. faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome escolhido

import random

a = input('nome aluno 1 ')
b = input('nome aluno 2 ')
c = input('nome aluno 3 ')
d = input('nome aluno 4 ')

al = random.choice([a, b, c, d])

print(f'o aluno {al} foi escolhido.')
