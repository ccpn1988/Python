print('\033[31m UTILIZANDO FOR ANINHADO \033[m')
print()

print('LOOPS ANINHADOS')
for i in range(0,5):
    for a in range(0,5):
        print(a)

print()
print('OPERANDO COM VALORES DE UMA LISTA COM LOOP FOR:')
listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i
print(soma)

print()
print('LOOPS FOR EM LISTAS DE LISTAS')
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
for valor in listas:
    print(valor)

print()
print('CONTANDO OS ITENS DE UMA LISTA')
lista = [5,6,10,13,17]
count = 0
for item in lista:
    count += 1
print(count)

print()
print('CONTANDO O NUMERO DE COLUNAS')
lst =[[1,2,3,4,5], [3,4,5], [5,6,7]]
# DEFININDO QUAL INDICE DA LISTA DEVE SER VALIDADA
primeira_linha = lst[0]
# VARIAVEL DE INCREMENTO
count = 0
# PERCORRENDO ITEM DA LISTA COM INDICE[0]
for column in primeira_linha:
    # INCREMENTANDO
    count = count + 1
print(count)

print()
print('PESQUISANDO EM LISTAS')
listaC = [5,6,7,10,50]
# LOOP ATRAVES DA LISTA
for item in listaC:
    if item == 5:
        print(f'Numero {item} encontrado na lista')

print()
print('LISTANDO AS CHAVES DE UM DICIONÁRIO')
dict = {'k1':'BACKUP', 'k2':'R', 'k3':'Scala'}
for item in dict:
    print(item)

print()
print('IMPRIMINDO CHAVE E VALOR DO DICIONARIO COM METODO ITEMS() PARA PEGAR OS ITENS DO DIC')
dict = {'k1':'BACKUP', 'k2':'R', 'k3':'Scala'}
for k,v in dict.items():
    print(k,v)
