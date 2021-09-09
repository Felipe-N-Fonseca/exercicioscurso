# refaça o exercicio 35 adicionando o dado de qual tipo de triangulo ele pode formar
# equilatero: todos os lados iguais; isóceles: dois lados iguais; escaleno: todos diferentes


print('-=' *20)
print('bem vindo ao analisador de triangulos')
print('ele ira analisar se suas retas podem formar um triangulo')
print('-=' * 20)

s1 = float(input('digite um seguimento: '))
s2 = float(input('digite outro seguimento: '))
s3 = float(input('digite o ultimo seguimento: '))
print('-=' * 20)

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('esse triangulo pode existir')

    if s1 == s2 and s1 == s3:
        print('esse é um triangulo equilatro')
    elif s1 == s2 and s1 != s3 or s2 == s3 and s2 != s1:
        print('esse é um triangulo isóceles')
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print('esse é um triangulo escaleno')

else:
    print('esse triangulo não pode existir')
print('-=' * 20)

print('obrigado por usar o analisador')