print('-=-' * 30)
print('     MÉDIA ESCOLAR     ')
print('-=-' * 30)
print('''Digite duas notas e
eu irei tirar a média entre elas.''')
n1 = float(input('Digite a sua primeira nota: ').strip)
n2 = float(input('Digite a sua segundaa nota: ').strip)
me = n1 + n2 / 2
print('Sua primeira nota foi {} e sua segunda nota foi {}!'.format(n1, n2))
if me <= 14:
    print('A sua média está boa, continue assim!')
else:
    print('A sua média está ruim, estude mais!')
print('--ENCERRANDO PROGRAMA--')
