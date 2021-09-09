# faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# ex: digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('digite um número de 0 a 9999: '))
# n = num + 10000
# n1 = str(n)

# print(f'a unidade é {n1[4]}')
# print(f'a dezena é {n1[3]}')
# print(f'a centena é {n1[2]}')
# print(f'o milhar é {n1[1]}')

# ou:

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# se eó dividir ele da um numero inteiro, mas quando pega o resto ele da o valor certo, usando a matematica

print(f'a unidade é {u}')
print(f'a dezena é {d}')
print(f'a centena é {c}')
print(f'o milhar é {m}')
