# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

sal_hora = float(input('Informe o seu salario por hora R$ '))
horas_trab = int(input('Informe a quantidade de horas trabalhadas nos mês...'))
salario = sal_hora * horas_trab
print(f'Com {horas_trab}H por mês e com salário/hora de R${sal_hora}, o seu salário bruto é de R${salario:.2f}')