# faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# quantidade de notas
# a maior nota
# a menor nota
# a média da turma
# a situação(opicional)
# adicione também as docstrings da função

def notas(*nota, sit=False):
    """
    analiza as notas passadas e retorna um dicionário com a nota maior, menor, média das notas e a situação
    :param nota: recebe as notas
    :param sit: recebe se deseja ou não mostrar a situação
    :return: um dicionário com todas as informações
    """
    dicionario = {}
    soma = 0
    nota = list(nota)
    nota = nota[0]
    nota.sort()
    dicionario['quantidade de notas'] = len(nota)
    dicionario['maior'] = nota[len(nota)-1]
    dicionario['menor'] = nota[0]
    for c in nota:
        soma += c
    soma /= len(nota)
    soma = float(f'{soma:.2f}')
    dicionario['média'] = soma
    if sit:
        if soma >= 6:
            dicionario['situação'] = 'aprovado'
        else:
            dicionario['situação'] = 'reprovado'
    return dicionario

lista = []
confirma = 's'
while confirma not in 'Nn':
    lista.append(float(input('digite uma nota: ')))
    confirma = input('deseja continuar? [s/n]: ').strip()
    while confirma not in 'SsNn':
        confirma = input('deseja continuar? [s/n]: ').strip()
s = input('deseja saber a situação? [s/n]: ')
if s in 'sS':
    s = True
else:
    s = False
print(notas(lista, sit=s))
