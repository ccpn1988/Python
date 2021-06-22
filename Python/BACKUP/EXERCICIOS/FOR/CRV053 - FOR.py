# PALINDROMO - INVERSÂO DE STRING
# FRASES LIDAS EM AMBOS SENTIDOS (SUBI NO ONIBUS)

# CRIANDO A FRASE REMOVENDO ESPAÇO EM BRANCO(ANTES E DEPOIS) E DEIXANDO MAIUSCULA
frase = str(input('Digite uma frase: ')).strip().upper()
# SEPARANDO A FRASE EM FORMA DE LISTA
palavras = frase.split()
# UNINDO A FRASE REMOVENDO OS ESPAÇOS INTERNOS
junto = ''.join(palavras)
inverso = ''

# INICIO É O TAMANHO DA FRASE -1 PARA PEGAR O ULTIMO CARACTERE
# FINAL É NEGATIVO P SER DECRESCENTE
# STEP É NEGATIVO P SER DECRESCENTE
for c in range(len(junto) -1, -1, -1):
    # COLOCANDO A FRASE AO CONTRARIO NA VARIAVEL INVERSO
    inverso += junto[c]
print(f'O inverso de {junto} é {inverso}')
# VALIDANDO SE A FRASE INVERSA É IGUAL A FRASE UNIFICADA (JUNTA)
if inverso == junto:
    print(f'Temos um PALINDROMO.')
else:
    print('A frase não é um PALINDROMO ')
