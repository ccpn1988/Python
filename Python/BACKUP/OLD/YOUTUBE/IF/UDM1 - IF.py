idade = int(input('Digite sua idade: '))
sexo = str(input('Digite o sexo M ou F: ')).upper()

#if idade > 18:
#    print('Você já tem que pagar suas contas')
#elif idade == 18:
#    print('Vai começar a se fuder agora')
#else:
#    print('Pode deixar que os seus Pais pagam a conta.')

if sexo == 'M':
    if idade >= 18:
        print('Homem maior de idade')
    else:
        print('Homem menor de idade')
elif sexo == 'F':
    if idade >= 18:
        print('Mulher maior de idade')
    else:
        print('Mulher menor de idade')
else:
    print('Sexo não definido')

print()
print('Testando IF de outra forma')

if idade >= 18:
    if sexo == 'M':
        print('Homem maior de idade')
    else:
        print('Mulher maior de idade')

elif idade < 18:
    if sexo == 'M':
        print('Homem menor de idade')
    else:
        print('Mulher menor de idade')
else:
    print('Sexo  não definido')

