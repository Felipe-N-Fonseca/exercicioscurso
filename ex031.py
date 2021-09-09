# desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

distancia = int(input('digite a distancia da viagem em km: '))

if distancia <= 200:
    resultado = distancia * 0.5
    print(f'o preço da passagem é R${resultado:.2f}')
else:
    resultad = distancia * 0.45
    print(f'o preço da passagem é R${resultad:.2f}')
