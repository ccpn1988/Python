# 049 - TABUADA

from time import sleep

num = int(input('Digite um número.... '))
print(f'Vamos efetuar a tabuada do número {num}')
sleep(1)
for i in range(0, 11):
    print(f'{num} x {i} = {num * i}')
