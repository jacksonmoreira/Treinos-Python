print('-=-' * 30)
print('     CALCULADOR DE VIAGEM     ')
print('-=-' * 30)
print('''Digite a distância da sua viagem!
Viajens até 500km terão o preço de R$0,50 por km rodado.
Viajens acima de 500km terão o preço de R$0,45 por km rodado''')
print('-' * 5)
dis0 = float(input('Digite a distância da sua viagem: '))
dis1 = dis0 * 0.50
dis2 = dis0 * 0.45
print('-' * 5)
print('A sua viagem será de {}km e custará:'.format(dis0))
if dis0 <= 500:
    print('A sua viagem custará R${:.2f}, aproveite!'.format(dis1))
else:
    print('A sua viagem custará R${:.2f}, aproveite!'.format(dis2))
print('--ENCERRANDO PROGRAMA--')
