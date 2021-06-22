# FATIAMENTO = SLICING
# INDICES SÃO DEFINIDOS POR string[n] sendo n (indice)
# INDICES SÃO INICIADOS POR 0 (ZERO)
# O UTLIMO NUMERO INSERIDO E DESCONSIDERADO [0:6] CONSIDERA A 5 POSICAO DA STRING

print('Trabalhando com fatiamento.... ')
# positivos   [012345678]
texto       = 'python s2'
print(texto)
print(texto[0:6])

# negativos  -[987654321]
texto2      = 'python s2'
print(texto2[2:6])
url = 'www.google.com.br/'
print(url[:-1])

# INDICES ALTERNADOS = string[ini:fim:step]
nova_string = texto2[0:6]
print(nova_string)
print(nova_string[:-1:2])

