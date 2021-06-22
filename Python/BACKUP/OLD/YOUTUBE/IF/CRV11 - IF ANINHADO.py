# IF ANINHADo

nome = str(input('QUal é seu nome: ')).upper()

if nome == 'CAIO':
    print(f'Seu nome é bonito, {nome} ')
elif nome == 'PEDRO' or nome == 'THIAGO' or nome == 'MARIA':
    print(f'{nome} é um nome bem popular no Brasil.')
elif nome in 'ANA CLAUDIA JESSICA JULIANA':
    print(f'{nome} é um belo nome Feminino...')
else:
    print(f'{nome}, é um nome simples')
print(f'Tenha um bom dia {nome}')
