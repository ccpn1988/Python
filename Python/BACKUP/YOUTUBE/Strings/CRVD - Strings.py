# STRINGS
print('Trabalhando com Strings... ')

frase = 'Curso em Video BACKUP'

# FATIAMENTO DE STRING

print(f'O indice 9 da frase "{frase}" é a letra: "{frase[9]}"')

# CONCATENANDO PRINT COM FATIAMENTO
print(f'Buscando dentro da frase "{frase}" entre o índice 9 à 14', end=' ')
print(f'temos a palavra: "{frase[9:14]}"')

# FUNÇÃO LEN - TAMANHO
print(f'A frase "{frase}" possuí o tamanho de {len(frase)} caracteres')

# FUNÇÃO COUNT - CONTANDO QUANTIDADE DE CARACTERE
print(f'Na frase "{frase}" temos {frase.count("o")} letras "O"')

# FUNÇÃO FIND - PESQUISA POSIÇÃO - SE VIER (-1) NÃO EXISTE A PALAVRA
print(f'A palavra "deo" esta inicianado na posição "{frase.find("deo")}" dentro da frase "{frase}"')

# FUNÇÃO BOLEANA
print(f'Existe a palavra "CURSO" dentro da frase "{frase}" ? {("Curso" in frase)}')

# FUNÇÃO REPLACE - REPLICA/ALTERA CARACTERES SEM ALTERAR NA ORIGEM
print(f'Usando "REPLACE" para alterar "BACKUP" para "Android" na frase "{frase}": {frase.replace("BACKUP", "Android")}')

# METODO UPPER - MAIUSCULA
print(f'Usando UPPER: {frase.upper()}')

# METODO LOWER - MINUSCULA
print(f'Usando LOWER: {frase.lower()}')

# METODO CAPITALIZE
print(f'Usando Capitalize: {frase.capitalize()}')

# METODO TITLE
print(f'Usando Title: {frase.title()}')

# STRIP - REMOVE ESPAÇOS
frase2 = '  Aprenda BACKUP  '
print(frase2)
print(f'Usando strip: {frase2.strip()}')

# RSTRIP - REMOVE ESPAÇOS
print(f'Usando rstrip: {frase2.rstrip()}')

# LSTRIP - REMOVE ESPAÇOS
print(f'Usando lstrip: {frase2.lstrip()}')

# SPLIT - QUEBRA FRASE EM LISTA ATRAVES DA CONDIÇÃO
print(frase.split(' '))
print(frase)
print(frase2.strip().split(' '))
print(frase2)

# JOIN - AGRUPA CONTEUDO EM FORMA DE LISTA
print(frase.split(' '))
print(' '.join(frase))

# PRINT PARA TEXTOS LONGOS (""" """)

print("""O Ministério da Saúde informou ao Supremo Tribunal Federal (STF), nesta terça-feira (15), 
que o governo prevê iniciar a vacinação contra a Covid-19 em até cinco dias após o registro ou autorização das doses 
pela Agência Nacional de Vigilância Sanitária (Anvisa) e a entrega dos primeiros lotes.""")

# ALTERANDO CONTEUDO DE STRING (STRINGS SAO IMUTAVEIS)
print(frase)
frase = frase.replace('BACKUP', 'Android')
print(frase)