idade = int(input('Digite sua idade: '))
sexo = input('Informe seu sexo: ').lower()
cidade = input('Informe sua cidade, apenas a sigla do Estado: ').lower()
estado = str(cidade[0:2]) -1
#
#if idade >= 18:
#    print('Voce e maior de idade')
#else:
#    print('Vc e menor, vaze pfv')

################################################################################################################################################################################################

#if idade > 18 and sexo == 'm':
#    print('Homem maior de idade ')
#elif idade < 18 and sexo == 'm':
#    print('Homem menor de idade')
#elif idade > 18 and sexo == 'f':
#    print('Mulher maior de idade')
#elif idade < 18 and sexo == 'f':
#    print('Mulher menor de idade')
#else:
#   ('Tem erro no codigo')

################################################################################################################################################################################################
if estado == 'RJ' or estado == 'SP' or estado == 'MG' or estado == 'ES':
    if idade >= 18:
        if sexo == 'm':
            print('Homem maior de idade, da regiao Sudeste')
        else:
            print('Mulher maior de idade, da regiao Sudeste')

    elif idade < 18:
        if sexo == 'f':
            print('Muher menor de idade,  da regiao Sudeste')
        else:
            print('Homem menor de idade,  da regiao Sudeste')

    else:
        print('Dados informados incorretamente')

else:
    print('Teste apenas para regisao Sudeste')

################################################################################################################################################################################################

