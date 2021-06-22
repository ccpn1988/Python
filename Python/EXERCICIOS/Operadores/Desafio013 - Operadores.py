# AUMENTO DE SALÁRIO 15%

from time import sleep
salario = float(input('Digite o salário a ser reajustado R$... '))
aumento = float(salario * 15/100)
nsal = salario + aumento
print('Caculando o reajuste')
sleep(1)

print(f'Com um reajuste de 15% sobre o salário de R$ {salario:.2f}, seu aumento será de: R$ {aumento:.2f} ', end='')
print(f' e seu novo salario será R$ {nsal:.2f}')
