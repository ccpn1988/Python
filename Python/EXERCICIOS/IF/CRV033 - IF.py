# INFORME 3 NUMEROS E MOSTRE O MAIOR E MENOR NUMERO....

a = int(input('Informe o primeiro numero: '))
b = int(input('Informe o segundo numero: '))
c = int(input('Informe o terceiro numero: '))
menor = a
maior = a
# VERIFICANDO MENOR NUMERO
if b<a and b<c:
    menor = b
if c<a and c<a:
    menor = c
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')