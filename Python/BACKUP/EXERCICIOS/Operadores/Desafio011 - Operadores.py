# LEIA ALTURA, LARGURA E A QTD DE TINTA PARA PINTAR A ÁREA....

from time import sleep
alt = int(input('Informe a altura... '))
lar = int(input('Informe a largura... '))
area = alt * lar
tinta = int(area / 2)

print('Calculando a quantidade de tinta para area informada.. ')
sleep(1)

print(f'Para uma área de {area}m é necessário {tinta}L de tinta')
