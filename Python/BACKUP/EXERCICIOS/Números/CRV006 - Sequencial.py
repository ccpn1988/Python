# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from time import sleep

raio = float(input('Digite o raio para calcular a area do círuclo: '))
area = 3.14 * (raio **2)
print('Calculando a área do círculo...')
sleep(1)

print(f'Para um raio de {raio:.2f} temos uma área de {area:.2f}m2')



