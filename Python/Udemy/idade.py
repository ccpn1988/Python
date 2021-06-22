estado = ['RJ', 'SP' , 'MG', 'ES']
idade = int(input('Digite sua idade ? '))
sexo = input('Digite o sexo M ou F : ') .upper()
cidade = str(input('Digite a sigla de seu Estado: ')).upper()

cidade_estado = str(cidade[1:3])-1

regiao = estado[cidade_estado]

if regiao:

    if sexo == 'M':
        if idade < 18:
            print('Homem menor de idade e da região Sudeste')
        else:
            print('Homem maior de idade e da região Sudeste')

    elif sexo == 'F':
        if idade < 18:
            print('Mulher menor de idade e da região Sudeste')
        else:
            print('Mulher maior de idade e da região Sudeste')

else:
    print('Teste apenas para a região Sudeste')

input('Pressione ENTER para sair do programa')
    
# if idade < 18 and sexo == 'M':
#    print('Homem menor de idade')

## elif idade <18 and sexo == 'F':
 #   print('Mulher menor de idade')

# elif idade >= 18 and sexo == 'M':
#    print('Homem maior de idade')

# elif idade >= 18 and sexo == 'F':
#    print('Mulher maior de idade')

# input('Precione ENTER para sair do programa')
