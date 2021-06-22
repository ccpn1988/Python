# Faça um Programa que converta metros para centímetros.

from time import sleep
area = float(input('Digite a metragem a ser cálculada: '))
cm = area * 100


print(f'Calculando {area}m informada em cm')
sleep(1)
print(f'A área de {area}m convertida em CM fica com um total de: {cm}cm')

