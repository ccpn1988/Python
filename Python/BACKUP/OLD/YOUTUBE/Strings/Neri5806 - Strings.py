nome = 'Neri Aldoir Neitzke'
print(nome)

# TAMANHO DA STRING - LEN
tam = len(nome)
print(f'Tamanho do nome {nome}: {tam} caracteres')

# CENTRALIZANDO COM ESPAÇOS EM BRANCO - CENTER
print(nome.center(25))

# PESQUISA A ULTIMA LETRA - ENDSWITH
print(nome.endswith('t'))

# PESQUISA A POSIÇÂO DO CARACTERE PESQUISADO - FIND
print(nome.find('ke'))
# PEGANDO A PARTIR DA POSIÇÂO DEFINIDA ('find', de, ate)
print(nome.upper().find('N',3))

# RETORNA POSIÇÂO - INDEX
print(nome.index('N'))
