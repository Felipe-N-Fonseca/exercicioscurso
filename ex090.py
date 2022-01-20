# faça um programa que leia nome e média de um aluno, guardando também a situação (aprovado ou reprovado)
# em um dicionario. no final mostre o conteudo da estrutura na tela media >= 7

aluno = {}
aluno['nome'] = str(input('digite o nome do aluno: ').strip())
aluno['média'] = float(input('digite a média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif aluno['média'] < 5:
    aluno['situação'] = 'reprovado'
else:
    aluno['situação'] = 'enviado a recuperação'
print(f"o aluno {aluno['nome']} foi {aluno['situação']} com média {aluno['média']}")
