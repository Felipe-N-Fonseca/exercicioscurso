# crie um programa que leia duas notas de um aluno e calcule sua média
# mostrando no final uma mensagem de acordo com a média atingida
# abaixo de 5: reprovado; entre 5 e 6,9: recuperação; 7 ou superior: aprovado

no1 = float(input('digite a primeira nota: '))
no2 = float(input('digite a segunda nota: '))

me = (no2 + no1) / 2

if me < 5:
    print(f'você foi reprovado com uma média de {me}')
elif me >= 5 and me < 7:
    print(f'você está de recuperação por sua média de {me}')
else:
    print(f'parabéns você passou cum uma média de {me}')
