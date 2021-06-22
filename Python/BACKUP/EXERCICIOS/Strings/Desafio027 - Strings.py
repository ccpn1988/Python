# PRIMEIRO E ULTIMO NOME DA PESSOA...

nome = str(input('Digite seu nome completo... ')).strip()

# QUEBRANDO O NOME EM LISTA:
n = nome.split(' ')

# PESQUISANDO PRIMEIO NOME:
print(f'Seu primeiro nome é : {n[0]}')

# PESQUISANDO ULTIMO NOME:
print(f'Seu ultimo nome é : {n[len(n)-1]}')

