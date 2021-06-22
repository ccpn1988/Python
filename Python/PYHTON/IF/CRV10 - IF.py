nome = str(input('Digite seu nome: '))

if nome == 'Caio':
    print(f'Que nome lindo você tem')
else:
    print('Seu nome é tão normal')

print(f'Bom dia, {nome}!')

print()
print('Validando notas:')

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) / 2

print(f'Sua média foi {m:.2f}')

if m >= 6.0:
    print('Sua média foi boa, PARABENS!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!!!')

print()
print('Testando Condição Simplificada....')

print('PARABENS' if m>=6 else 'ESTUDE MAIS')