# faça um programa que peça o sexo de uma pessoa mas só aceite valores 'm' ou 'f',
# caso esteja errado peça a digitação novamente até ter um valor correto

sexo = str(input('digite seu sexo [m/f]: ')).strip().lower() [0]

while sexo not in 'mf':
    sexo = str(input('digite um valor valido [m/f]: ')).strip().lower() [0]
