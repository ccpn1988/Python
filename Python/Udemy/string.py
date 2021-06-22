nome = ' caio '
sobrenome_mae = 'Almeida'
sobrenome_pai = 'Neves'
empresa = 'grupogen.com.br'
idade = 32

print(nome.title())
print(nome.upper())
print(nome.lower())
print(nome.rstrip()) 
print(nome.lstrip()) 
print(nome.strip())  
print('O analista',nome.title(), 'tem',str(idade), 'anos')




iniciais = nome[0] + sobrenome_mae[0] + sobrenome_pai[0]
print(iniciais)

email = nome + '.'+ sobrenome_pai + '@' + empresa
print(email)