# STRINGS

# CARLOS MELO - SIGMOIDAL

# ASSOCIANDO STRINGS AS VARIAVEIS
nome = 'Carlos'
sobrenome = 'Melo'
sufixo = 'Junior'
profissão = 'Piloto'

# Imprimindo nome completo - Concatenado
print('Nome Completo')
print(nome + " " + sobrenome + " " + sufixo)

# Imprimindo Profissão - Metodo Antigo
print('Sua profissão é:',profissão + '.')

# INDICE COMEÇA POR ZERO
print(f'A primeira letra do nome {nome} é: {nome[0]}')
print(f'A ultima letra do nome {nome} é: {nome[-1]}')


# FUNÇÔES
# LEN - TAMANHO DA STRING
dna = 'ATERFDGDLHDABHSDB'
print(f'O tamanho da variável {dna} é de: {len(dna)}')

# SPLIT - QUEBRA EM PEDAÇÔS DE ACORDO COM A CONIÇÂO DO SEPARADOR (GERA UMA LISTA)
nomes = 'Carlos, Fernando, Theo'
print(f'Quebrando a variavel através do separador virgula',end=' ')
print(nomes.split(','))
print(nomes.split(',')[0])
print(nomes.split(',')[1])
print(nomes.split(',')[2])

# REPLACE = SUBSTITUI UM VALOR POR OUTRO
valor = "9,50"
valor = valor.replace(",", ".")
print(valor)

# STRIP - REMOVE ESPAÇOS EM BRANCOS OU CARACTERES
nome = "    CAIO NEVES  "
print(f'O nome {nome} sem a função strip tem {len(nome)} caracteres')
print(f'O nome {nome} com a função strip tem {len(nome.strip())} caracteres')

var = 'R$ 9,50'
var = float(var.strip('R$ ').replace(",", "."))
print(var)
print(type(var))

# SLICING - CORTAR STRINGS - FATIAMENTO
num = '123456789'
print(f'Pegando apenas os numeros ímpares: {num[::2]}')
print(f'Pegando apenas os numeros pares: {num[1::2]}')

# CAPITALIZE = TRANSFORMA 1° CARACTERE EM MAIUSCULO
nome = 'Jose Santos DA SILVA'
print(f'Utilizando CAPITALIZE: {nome.capitalize()}')

# LOWER = TRANSFORMA TUDO EM  MINUSCULO
nome = 'JOSE SANTOS DA SILVA'
print(f'Utilizando LOWER: {nome.lower()}')

# UPPER = TRANSFORMA TUDO EM MAIUSCULO
nome = 'JOSE SANTOS DA SILVA'
print(f'Utilizando UPPER: {nome.upper()}')

# TITLE = TRANSFORMA 1 LETRA DE CADA PALAVRA EM MAIUSCULO
nome = 'JOSE SANTOS DA SILVA'
print(f'Utilizando TITLE: {nome.title()}')

# SWAPCASE = INVERTE MAIUSCULA EM MINUSCULA
nome = 'Jose Santos DA SILVA'
print(f'Utilizando SWAPCASE: {nome.swapcase()}')