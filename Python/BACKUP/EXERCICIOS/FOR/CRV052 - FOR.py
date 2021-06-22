# 052 - NUMEROS PRIMOS = DIVISIVEL APENAS POR 1 E POR ELE MESMO
# LER UM NUMERO INTEIRO E VALIDAR SE E UM NUMERO PRIMO

num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[34m', end=' ')
        tot += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[mO numero {num} é divisivel {tot} vezes')
if tot == 2:
    print(f'Por isso ele é PRIMO')
else:
    print(f'Por isto ele não é PRIMO')
