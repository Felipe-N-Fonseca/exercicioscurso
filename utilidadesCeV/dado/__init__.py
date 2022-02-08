def leiadinheiro(msg):
    d = input(msg).replace(',', '.').strip()
    while d.isalpha():
        print(f'\033[1;31mERRO!!! {d} não é um valor válido\033[m')
        d = input(msg).replace(',', '.').strip()
    d = float(d)
    return d
