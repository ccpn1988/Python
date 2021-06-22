# 059 - CRIANDO MENU DE OPÇÔES
# LER 2 NUMEROS E REALIZAR A OPÇÂO ABAIXO
# MOSTRAR UM MENU
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NUMEROS
# [5] SAIR DO PROGRAMA

num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
print('''Opções: 
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA ''')
opcao = int(input('Digite a opção e ser executada: '))

while opcao != 5:
    if opcao == 1:
        print(f'Você selecionou a opção {opcao} SOMAR')
        print(f'A soma entre {num1} + {num2} é: {num1 + num2}' )
        opcao = int(input('''Digite a opção e ser executada: 
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA 
        Digite sua opção: '''))
    elif opcao == 2:
        print(f'Você selecionou a opção {opcao} MULTIPLICAR')
        print(f'A soma entre {num1} * {num2} é: {num1 * num2}')
        opcao = int(input('''Digite a opção e ser executada: 
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA 
        Digite sua opção: '''))
    elif opcao == 3:
        if num1 > num2:
            print(f'Você selecionou a opção {opcao} MAIOR')
            print(f'O maior número entre {num1} e {num2} é: {num1}')
        else:
            print(f'Você selecionou a opção {opcao} MAIOR')
            print(f'O maior número entre {num1} e {num2} é: {num2}')
        opcao = int(input('''Digite a opção e ser executada: 
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA 
        Digite sua opção: '''))
    elif opcao == 4:
        print(f'Você escolheu a opção {opcao}...Escolha novos números: ')
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        opcao = int(input('''Digite a opção e ser executada: 
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA 
        Digite sua opção: '''))
    elif opcao == 5:
        print(f'Você escolheu a opção {opcao}...Finalizando: ')
    else:
        print(f'Você escolheu a opção {opcao}...Opção Inválida: ')
print('Fim do programa!!!')