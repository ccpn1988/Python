x = 0
while x < 5:
    if x == 3:
        x += 1
        #continue
        break
    print(x)
    x += 1
print('ACABOU')

print('######################################################################################################################')
print()

x = 0 # coluna

while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'({x} e {y})')
        y += 1

    x += 1
print('Acabou !!!')
print('######################################################################################################################')
print()

# ACUMULADORES
# CONTADORES

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no Else.')
