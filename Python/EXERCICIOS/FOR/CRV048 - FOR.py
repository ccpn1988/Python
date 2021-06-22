# 048 - SOME TODOS OS NUMEROS IMPARES MULTIPLOS DE 3 NO INTERVALO DE 1 A 500
print('-*-' * 5)
print('EXERCICIO 048 ')
print('-*-' * 5)
print()

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print(f'A soma de todos os {cont} valores divisiveis por 3 seu total é: {soma}')
