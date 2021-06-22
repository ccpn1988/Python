# SPLIT - DIVIDE UMA STRING - .split('separador')


print('Split - Join - Enumerate... ')

string = 'O Brasil é o país do futebol, o Brasil é Penta!'
lista = string.split(' ')
print(lista)
lista2 = string.split(',')
print(lista2)

for valor in lista:
    print(f'A palavra "{valor}" apareceu {lista.count(valor)}x vezes')

palavra = ' '
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi {palavra} {contagem}x')
