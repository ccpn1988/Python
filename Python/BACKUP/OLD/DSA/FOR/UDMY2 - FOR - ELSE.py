print('FOR/ELSE EM OLD')

variavel = ['Caio','Cesar','Pereira','Neves']

for valor in variavel:
    print(valor)

print()
for nome in variavel:
    # startswith = VERIFICA SE UM VALOR DA STRING COMEÇA COM LETRA ESPECIFICA
    if nome.startswith('C'):
        print(f'Começa com C: {nome}')
    else:
        print(f'Não começa com C: {nome}')

print()
for name in variavel:
    if name.startswith('N'):
        break
    else:
        print(f'Não existe uma palavra com N: {name}.')