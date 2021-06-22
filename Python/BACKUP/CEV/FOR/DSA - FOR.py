print('\033[32m FOR - VALIDA CADA ITEM EM UMA SERIE DE VALORES, DETERMINADAS VEZES. \033[m')

# $ for item in serie-de-itens
        # if item > 0:
            # EXECUTAR COMANDOS

# PODE SER UTILIZADO EM (STRINGS, LISTAS, TUPLAS, ELEMENTOS DE DICIONÁRIOS, ARQUIVOS)
# UTILIZADO PARA EXECUÇÃO POR VARIAS VEZES.
print()
print('FOR USANDO TUPLAS')
print('CRIANDO TUPLA E IMPRIMINDO SEUS VALORES:')
tp = (2,3,4)
for i in tp:
    print(i)

print()
print('FOR USANDO LISTAS')
print('CRIANDO UMA LISTA E IMPRIMINDO CADA UM DOS VALORES:')
lista = ['LEITE','FRUTAS','ARROZ','CARNE','BEBIDAS']
for i in lista:
    print(f'\033[31m {i} \033[m')

print()
print('FOR USANDO CONTADORES(RANGE)')
print('IMPRIMINDO OS VALORES NO INTERVALO ENTRE 0 E 5 ')
for contador in range(0,5):
    print(contador)

print()
print('IMPRIMINDO NA TELA APENAS NUMEROS PARES DA LISTA')
n1 = [1,2,3,4,5,6,8,9,10]
for num in n1:
    if num % 2 == 0:
        print(num)

print()
print('LISTANDO OS NUMEROS NO INTERVALO ENTRE 0 E 101, INCREMENTANDO 2')
for i in range(0,101,2):
    print(i)

print()
print('UTILIZANDO FOR COM STRINGS')
for caracter in 'BACKUP é uma linguagem de programação divertida':
    print(caracter)