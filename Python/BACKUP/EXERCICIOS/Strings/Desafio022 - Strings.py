# PROGRAMA QUE LEIA O NOME E MOSTRE
# MAIUSCULA
# MINUSCULA
# QTD DE LETRAS SEM ESPAÇOS
# QTD DE LETRAS O 1° NOME

print('Trabalhando com strings...')

nome = str(input('Digite seu nome completo... '))

print(f'Seu nome em maíusculo é: {nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')
print(f'Seu nome completo sem espaços possuí: {len(nome.strip())-nome.count(" ")} letras')

print(f'Seu 1 nome tem {nome.find(" ")} letras')
nome2 = nome.split(" ")
print(f'seu 1 nome tem {len(nome2[0])} letras')