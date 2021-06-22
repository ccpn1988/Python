# str - STRING

nome = 'Caio Neves'
idade = 32
altura = 1.77
peso = 107
imc = peso / (altura ** 2)
ano_atual = 2020
nasc = ano_atual - idade

print(f'{nome} tem {idade} anos,nasceu no ano de {nasc}, possuí {altura}m pesa {peso}kg e seu IMC é de {imc:.2f}')

# TROCANDO VALORES DE VARIAVEIS

x = 10
y = 'CAIO'
x,y = y, x

# OPERADOR TERNARIO

logged_user = False
msg = 'Usuáior logado. ' if logged_user else 'Usuário não logado.'
print(msg)

idade = input('Digite sua idade.. ')

if not idade.isnumeric():
    print('Favor digitar em formato numérico... ')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'É de maior, pode acessar' if e_de_maior else 'Não pode acessar. '

    print(msg)
input('Aperte ENTER para encerrar o programa.')
