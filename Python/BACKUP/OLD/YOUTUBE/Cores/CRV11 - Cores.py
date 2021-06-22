# CORES NO TERMINAL
# ANSI - ESCAPE SEQUENCE = \033[style;text;backm = \033[0;33;44 m

# STYLE = 0 = NADA / 1 = BOLD / 4= UNDERLINE / 7 = negativo
# TEXT = 30 ao 37
# BACK = 40 a 47

# \033[7;30m
# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[m

print('\033[1;33m Olá, Mundo')
print('\033[4;30;45m Olá MUndo! \033[m')

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
print(f'Os numeros digitados são \033[31m{a}\033[m e \033[34m{b}\033[m !!!!')

nome = str(input('Digite seu nome: '))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m'}
print(f'O nome digitado foi {cores["amarelo"]} {nome}')
print(f'O nome digitado foi {cores["vermelho"]} {nome}')