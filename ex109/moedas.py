def aumentar(n, a, m=False):
    n *= ((100 + a)/100)
    if m:
        return moeda(n)
    else:
        return n


def diminuir(n, d, m=False):
    n *= ((100 - d)/100)
    if m:
        return moeda(n)
    else:
        return n


def dobrar(n, m=False):
    n *= 2
    if m:
        return moeda(n)
    else:
        return n


def metade(n, m=False):
    n /= 2
    if m:
        return moeda(n)
    else:
        return n

def moeda(n, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')
