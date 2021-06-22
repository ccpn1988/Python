# ALUGUEL DE CARROS
dias = int(input('QUantos dias de locação? '))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é R${pago:.2f}')
