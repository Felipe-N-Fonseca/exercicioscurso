# melhore o ex061 perguntando para o usuario se ele quer mostrar mais alguns termos, o programa encerrq
# quando o usuario digitar que não quer mais nenhum termo

termo = int(input('digite o termo: '))
razao = int(input('digite a razão: '))
p = 's'

while p not in 'n':
    for c in range(10, 0, -1):
        if c > 1:
            print(termo, end= ' -> ')
        else:
            print(termo)
        termo += razao
    p = str(input('deseja continuar? [s/n]: ')).strip().lower()
