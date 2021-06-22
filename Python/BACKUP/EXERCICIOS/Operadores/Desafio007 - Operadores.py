# CALCULE A MEDIA

from time import sleep

nota1 = float(input('Digite a primeira nota...'))
nota2 = float(input('Digite a segunda nota...'))
media = (nota1 + nota2) / 2

print(f'A primeira nota foi: {nota1}')
print(f'A segunda nota foi: {nota2}')
print('Calculando sua média..')
sleep(1)
print(f'A meédia entre as notas {nota1} + {nota2} é de: {media}')

