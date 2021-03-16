from random import randint
print('#' * 30)
print('     SORTEADOR AUTOMÁTICO     ')
print('#' * 30)
print('=' * 45)
print('''Digite o que ou quem
participará do sorteio, se for
digitar um número, escreva-o por extenso!''')
print('-' * 20)
print('''AVISO: Número máximo de integrantes
do sorteio: 5!''')
print('-' * 20)
mot = str(input('Digite para qual motivo o sorteio será realizado: ').lower())
co1 = str(input('Digite a primeira coisa a ser sorteada: ').strip())
co2 = str(input('Digite a segunda coisa a ser sorteada: ').strip())
co3 = str(input('Digite a terceira coisa a ser sorteada: ').strip())
co4 = str(input('Digite a quarta coisa a ser sorteada: ').strip())
co5 = str(input('Digite a quinta coisa a ser sorteada: ').strip())
lis = [co1, co2, co3, co4, co5]
lis1 = lis[randint(0, len(lis))]
print('O sorteado para {}, foi:'.format(mot))
print('{}!'.format(lis1))
print('-' * 20)
print('--ENCERRANDO PROGRAMA--')
print('=' * 45)
