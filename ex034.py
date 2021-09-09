# escreva um programa que pergunte o salario de um funcionario e calcule seu valor de aumento.
# para salarios superiores a R$ 1.250,00 calcule um aumento de 10%
# para os inferiores ou iguais o aumento é de 15%

salario = float(input('digite o salario do seu funcionario: '))

if salario <= 1250.00:
    print(f'o salario com aumento será de {salario * 1.15:.2f }')
else:
    print(f'o salario do funcionario com aumento é igual a {salario * 1.10 :.2f}')
