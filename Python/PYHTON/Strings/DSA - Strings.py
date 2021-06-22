print('Criando uma string em BACKUP!! ')
# QUEBRANDO LINHAS
print('Testando \n Strings \n em \n BACKUP')
print('Testando \nStrings \nem \nBACKUP')

s = 'Data Science Academy'
print(s)
# PEGANDO INDICES
print(s[0])
print(s[1])
print(s[2])
print(s[3])

#SLICING - TUDO ATÈ A POSIÇÃO 4 SEM CONSIDERAR A POSIÇÃO 4 (D A T A)
print(s[0:4])
print(f'Imprimindo "Data" via slicing....',s[:4])
# RETORNANDO A STRING COMPLETA PEGANDO TODAS AS POSIÇÕES [::1]
print(s[::1])

# PROPRIEDADES DE STRING - Não permitido alterar
# s[0] = 'x'
#print(s)

# CONCATENAÇÃO
print(s)
s = s + ' é a melhor maneira de estar preparado para o mercado de Ciência de Dados'
print(s)


# FUNÇÕES BUILT-IN STRINGS
print('UPPER - MAIUSCULA - ',s.upper())
print('LOWER - MINUSCULA - ',s.lower())
print('CAPITLIZE - 1 LETRA MAIUSCULA - ',s.capitalize())
print('ISLOWER - SE HA MINUSCULO = TRUE/FALSE - ',s.islower())
print('SPLIT - QUEBRA POR ESPAÇOS EM BRANCO CONFORME (caractere)', s.split('y'))
print('SPLIT - QUEBRA POR ESPAÇOS EM BRANCO CONFORME TRANSFORMANDO EM "LISTAS"', s.split())
print('COUNT - CONTA QTD DE CARACTERES', s.count('a'),' PESQUISANDO LETRA "A"')
print('FIND - PESQUISA LETRA', s.find('a'), 'PESQUISANDO POSIÇÃO DA 1° LETRA "A"')
print('ENDSWITH - SE TERMINA COM A ULTIMA LETRA - TRUE/FALSE "', s.endswith('a'), '"PESQUISANDO SE TERMINA COM A LETRA "A"')