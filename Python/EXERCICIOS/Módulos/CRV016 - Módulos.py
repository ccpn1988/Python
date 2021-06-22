import math
from math import trunc
num = float(input('Digite um numero com casas decimais: '))

print(f'O número digitado foi {num}, ele em sua porção inteira é {math.trunc(num)}')
print(f'O número digitado foi {num}, ele em sua porção inteira é {trunc(num)}')

# SEM MÓDULOS
num = float(input('Digite um numero: '))
print(f'O valor digitado foi {num} e sua parte inteira {int(num)}')
