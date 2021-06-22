compras = ['arroz', 'feijao', 'macarrão', 'carne']
nome = 'Joaquim'
print('FOR LOOP COM LISTAS')
for i in compras:
    print(i)
print('#' * 25)
for i in nome:
    print(i)
print('#' * 25)
vendas = [1000, 450, 300, 920, 600]
total = 0
for i in vendas:
    total += i
    print('IMPRIMINDO A SOMATORIA')
    print(total)
print('IMPRIMINDO TOTAL')
print(total)

print('#' * 25)
print('FOR LOOP COM DICIONARIOS')
cores = {'verde':'green', 'preto':'black', 'azul':'blue'}
print('IMPRIMINDO CHAVES')
for i in cores:
    print(i)
print('#' * 25)
print('IMPRIMINDO CHAVES e VALORES CONFORME DICIONARIO')
for i in cores.items():
    print(i)
print('#' * 25)
print('IMPRIMINDO CHAVES E OS VALORES')
for k,v in cores.items():
    print(k,v)
print('#' * 25)
print('IMPRIMINDO APENAS OS VALORES')
for i in cores:
    print(cores[i])

print('#' * 28)
print('IMPRIMINDO CHAVES E OS VALORES')
for i in cores:
    print(i, cores[i])