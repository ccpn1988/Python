# AUMENTOS MULTIPLOS

salario = float(input('Digite o salário a ser calculado: '))

if salario > 1250:
    salario = salario + (salario /100) * 10
    #salario = salario + (salario * 10 / 100)
    print(f'Com aumento de 10% seu salário fica em R$: {salario:.2f}')
else:
   salario = salario + (salario / 100) * 15
   # salario = salario + (salario * 15 / 100)
   print(f'Com aumento de 15% seu salário fica em R$: {salario:.2f}')