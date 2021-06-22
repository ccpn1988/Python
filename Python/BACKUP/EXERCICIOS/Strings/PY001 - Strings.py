# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo

print('STRINGS')
print()
string1 = 'Brasil Hexa 2006'
string2 = 'Brasil! Hexa 2006!'

# CONTANDO O TAMANHO DA STRING DESCONSIDERANDO O ESPAÇO EM BRANCO NO TEXTO:
print(f'O tamanho de "{string1}" é de: {len(string1.strip()) - string1.count(" ")} caracteres.')
print(f'O tamanho de "{string2}" é de: {len(string2.strip()) - string2.count(" ")} caracteres.')

print('Comparando as strings... ')

if len(string1) == len(string2):
    print('As strings possuem o mesmo tamanho e conteúdo.... ')
else:
    if string1 == string2:
        pass
    else:
        print('As duas strings possuem conteúdos diferentes...')
    print('As duas strings são de tamanhos diferentes... ')

print('MANEIRA 2')
if len(string1) != len(string2):
    if string1 == string2:
        pass
    else:
        print('As duas strings possuem conteúdos diferentes...')
    print('As duas strings são de tamanhos diferentes... ')
else:
    print('As strings possuem o mesmo tamanho e conteúdo.... ')

print('MANEIRA 3')

if len(string1) != len(string2):
    if string1 != string2:
        print('As duas strings possuem conteúdos diferentes...')
    else:
        pass
    print('As duas strings são de tamanhos diferentes... ')
else:
    print('As strings possuem o mesmo tamanho e conteúdo.... ')