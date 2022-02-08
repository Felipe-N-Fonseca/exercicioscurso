def aumentar(n, a, m=True):
    n *= ((100 + a)/100)
    if m:
        return moeda(n)
    else:
        return n


def diminuir(n, d, m=True):
    n *= ((100 - d)/100)
    if m:
        return moeda(n)
    else:
        return n


def dobrar(n, m=True):
    n *= 2
    if m:
        return moeda(n)
    else:
        return n


def metade(n, m=True):
    n /= 2
    if m:
        return moeda(n)
    else:
        return n


def moeda(n, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


def resumo(n, a, d, m=True):
    print('_'*30)
    print(f"{'resumo do valor':^30}")
    print('_'*30)
    print(f'{" valor analisado: ":<18}{moeda(n)}')
    print(f'{" valor dobrado: ":<18}{dobrar(n,m)}')
    print(f'{" metade do valor: ":<18}{metade(n,m)}')
    print(f'{f" {a}% aumentado: ":<18}{aumentar(n,a,m)}')
    print(f'{f" {d}% diminuido: ":<18}{diminuir(n,d,m)}')
    print('_'*30)