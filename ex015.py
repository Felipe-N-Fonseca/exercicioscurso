# pergunte os km percorridos e os dias alugado e calcule o preço. sabendo que dia = 60 e km = 0.15
km = float(input('quantos km você andou? '))
d = int(input('quantos dias o carro ficou com você? '))
vkm = km * 0.15
vd = d * 60
print(f'o valor a ser pago por usar o carro por {d} dias e por {km}km é de R${vd+vkm :.2f}')
print(f'valor pelos km = R${vkm :.2f}')
print(f'valor pelos dias = R${vd :.2f}')
