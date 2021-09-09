# leia a altura e largura de uma parede em metros e mostre sua area e
# quantos litros de tinta se precisa para pintar, sabendo que cada litro pinta 2m²
l = float(input('digite a largura da parede em metros '))
h = float(input('digite a altura da parede em metros '))
t = 2
m = l * h
q = m / t
print(f'sua parede tem uma area de {m}m², e você precisa de {q}l de tinta pra pinta-la')
