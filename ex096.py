# faça um programa que tenha uma função área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a area do terreno

def area(a,b):
    multi = a * b
    print(f'a área é de {multi}m²')


print('-='*20)
print(f"{'calculadora de área':^40}")
print('-='*20)
area(float(input('largura (m): ')), float(input('comprimento (m): ')))
