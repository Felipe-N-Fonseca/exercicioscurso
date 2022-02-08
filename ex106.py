# faça um mini sistema que ultilize o interactive help do python. o usuario vai digitar o comando e o
# manual vai aparecer. quando o usuario digitar a palavra fim o programa se encerrará.
# obs: use cores

print('\033[1;30;43m-='*20)
print('sistena de ajuda do pyhton')
print('\033[1;30;43m-='*20)
c = input('\033[0;0mdigite o nome do comando (fim encerra): ').strip().lower()
while c not in 'fim':
    print('\033[1;30;107m', end='')
    help(c)
    c = input('\033[0;0mdigite o nome do comando (fim encerra): ').strip().lower()
print('\033[1;30;42mobrigado por me usar :)')
