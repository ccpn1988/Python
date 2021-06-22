# EXIBA O VALOR EM METROS,CM e MM

from time import sleep

print('-=-' * 10)
print('Calculando metragem, cm e mm')
print('-=-' * 10)

metros = float(input('Digite a metragem a ser calculada.. '))
cm = metros *100
mm = metros *1000

print(f'A metragem digitada foi {metros}m')
print('Convertendo a metragem informada')
sleep(1)
print(f'{metros}m, equivale há {cm}cm')
print(f'{metros}m, equivale há {mm}mm')

