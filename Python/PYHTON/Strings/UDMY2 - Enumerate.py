# ENUMERATE - ENUMERA ELEMENTO DE UMA LISTA

print('Trabalhando com ENUMERATE... ')

lista = ['CAIO', 'CESAR', 'PEREIRA', 'NEVES']
print(lista)

for ind, item in enumerate(lista):
    print(ind, item)

# LISTA DENTRO DE LISTAS
lista1 = [
    # INDICE 0 , 1 , 2
    ['Edu', 'João', 'Luiz'],  # INDICE 0
    ['Maria', 'Aline0','Joana'], # INDICE 1
    ['Helena','Ed', 'Lu'] # INDICE 2
]
# IMPRIMINDO JOANA [INDICE 1] [INDICE 2]
print(lista1[1][2])

# USANDO ENUMERATE INICIANDO EM ZERO
for v1,v2 in enumerate(lista1):
    print(v1,v2)
# ENUMERANDO A PARTIR DO 3
for v1, v2 in enumerate(lista1,3):
        print(v1, v2)

