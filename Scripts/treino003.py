print('-=-' * 30)
print('     MAIOR E MENOR NÚMERO     ')
print('-=-' * 30)
print('''Digite três números e eu informarei
qual o maior e qual o menor!''')
print('-' * 5)
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
print('Os números digitados foram, respectivamente {}, {} e {}.'.format(num1, num2, num3))
if num1 > num2 and num1 > num3:
    print('O maior número é {}!'.format(num1))
if num2 > num1 and num2 > num3:
    print('O maior número é {}!'.format(num2))
if num3 > num1 and num3 > num2:
    print('O maior número é {}!'.format(num3))
if num1 < num2 and num1 < num3:
    print('O menor número é {}!'.format(num1))
if num2 < num1 and num2 < num3:
    print('O menor número é {}!'.format(num2))
if num3 < num1 and num3 < num2:
    print('O menor número é {}!'.format(num3))
print('--ENCERRANDO-PROGRAMA--')
