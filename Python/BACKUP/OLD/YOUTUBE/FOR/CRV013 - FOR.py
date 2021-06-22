# AULA 13 - FOR

print('Oi')

for c in range(0, 6):
    print('OI')
print('FIM')

n = int(input('Digite um numero: '))

for c in range(0, n+1):
    print(c)
print('FIM')

print('Exemplo para TABUADA ')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for n in range(i, f+1, p):
    print(n)
print('LOOP FINALIZADO')

print('#$' * 10)
print('EFETUANDO SOMA COM FOR')

soma = 0
for i in range(0,3):
    n = int(input('Digite um número: '))
    soma += n
print(f'A soma dos valores acima é: {soma}')