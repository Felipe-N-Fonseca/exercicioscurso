#faça um programa que leia o comprimento dos catetos de um triangulo e calcule a hipotenusa
ca = float(input('digite o cateto adjacente '))
co = float(input('digite o cateto oposto '))
h = ((ca ** 2) + (co ** 2)) ** (1/2)
print(f'o valor da hipotenusa é {h:.f2}')

# na biblioteca math tem o modulo hypot que calcula a hipotenusa ja
