# https://docs.python.org/3.8/library/math.html#math.radians
import math
from math import radians, sin, cos, tan
ang = float(input('Digite o ãngulo que você deseja: '))
seno = math.sin(math.radians(ang))
seno1 = sin(radians(ang))
print('SENO....')
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
print('Usando apenas os módulos especificos....')
print(f'O ângulo de {ang} tem o SENO de {seno1:.2f}')

cosseno = math.cos(math.radians(ang))
cos = cos(radians(ang))
print('COSSENO.....')
print(f'O ângulo de {ang} tem o COSSENO de {cosseno:.2f}')
print('Usando apenas os módulos especificos....')
print(f'O ângulo de {ang} tem o COSSENO de {cos:.2f}')

tangente = math.tan(math.radians(ang))
tang = tan(radians(ang))
print('TANGENTE...')
print(f'O ângulo de {ang} tem o TANGENTE de {tangente:.2f}')
print('Usando apenas os módulos especificos....')
print(f'O ângulo de {ang} tem o TANGENTE de {tang:.2f}')