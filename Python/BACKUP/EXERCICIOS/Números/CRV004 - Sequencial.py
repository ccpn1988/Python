# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

from time import sleep

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
nota3 = float(input('Digite a 3° nota: '))
nota4 = float(input('Digite a 4° nota: '))

media = (nota1 + nota2 + nota3 + nota4) /4
print('Calculando as medias...')
sleep(1)
print(f'A média das notas bimestrais é: {media:.2f}')