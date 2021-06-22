# VALIDAR SE A CIDADE DIGITADA INICIA COM O NOME SANTO:

cidade = str(input('Digite a cidade em que nasceu... ')).strip()
print(cidade[:5].upper() == 'SANTO')
