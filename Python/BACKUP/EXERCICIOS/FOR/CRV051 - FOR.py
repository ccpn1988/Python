# 051 - DESENVOLVA UM PROGRAMA QUE LEIO O PRIMEIRO TERMO E A RAZAO DE UMA PROGRESSAO ARITMETICA.
# NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS.

print('==' * 20)
print('10 TERMOS DE UMA PROGRESSÃO ARITMETICA')
print('==' * 20)
print()

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão para progressão: '))
termo10 = primeiro + (10 - 1) * razão

for pa in range(primeiro, termo10 + razão, razão):
    print(f'{pa}', end='-> ')
print('TERMINO')