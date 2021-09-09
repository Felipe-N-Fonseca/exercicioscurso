# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status
# de acordo com a tabela abaixo
# abaixo de 18,5: abaixo do peso; entre 18,5 e 25: peso ideal; 25 até 30: sobrepeso; 30 até 40: obesidade;
# acima de 40: obesidade morbida

peso = float(input('qual seu peso em kg: '))
altura = float(input('qual sua altura em metros: '))

imc = peso / altura ** 2

print(f'seu imc é de {imc:.2f}')

if imc <= 18.5:
    print('abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('peso ideal')
elif imc > 25 and imc <= 30:
    print('sobrepeso')
elif imc > 30 and imc <= 40:
    print('obesidade')
else:
    print('obesidade morbida')
