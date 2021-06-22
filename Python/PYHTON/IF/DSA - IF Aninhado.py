# IF COM ESTRUTURA ANHINHADOS

idade = 18

if idade > 17:
    print('Você pode dirigir ')

nome = 'Bob'

print()
print('Testando condição aninhada.....')
if idade > 13:
    if nome == 'Bob':
        print('Ok Bob, você esta autorizado a entrar ')
    else:
        print("Desculpe, mas você não pode entrar! ")

print()
print('Utilizando operador logico (AND)')
if idade >= 13 and nome == 'Bob':
    print('Ok Bob, você esta autorizado a entrar...')
print()
print('Utilizando operador logico (OR)')
if (idade <= 13) or (nome == 'Bob'):
    print('Ok Bob, você esta autorizado a entrar... ')