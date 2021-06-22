nome = 'Caio'
sobrenome = 'Cesar Pereira Neves'

print(len(nome + ' ' + sobrenome))

print(f'Seu nome é {nome} e a primeira letra do seu nome é: "{nome[0]}" e o indice dela é 0')
print(f'Seu nome é {nome} e a segunda letra do seu nome é: "{nome[1]}" e o indice dela é 1')
print(f'Seu nome é {nome} e a terceira letra do seu nome é: "{nome[2]}" e o indice dela é 2')
print(f'Seu nome é {nome} e a quarta letra do seu nome é: "{nome[3]}" e o indice dela é 3')

print(f'Seu sobrenome é {sobrenome} e seu 1° sobrenome é: {sobrenome.split()[0]}')
print(f'Seu sobrenome é {sobrenome} e seu 1° sobrenome é: {sobrenome.split()[1]}')
print(f'Seu sobrenome é {sobrenome} e seu 1° sobrenome é: {sobrenome.split()[2]}')

