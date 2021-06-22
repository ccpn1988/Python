# 049 -

from time import sleep

print('-*-' * 5)
print('EXERCICIO 049 ')
print('-*-' * 5)
print()

num = int(input('Digite um numero para calcular a Tabuada: '))

for tab in range(0, 11):
    print(f'{num} x {tab} = {num * tab}')
