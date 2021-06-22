print('LOOP FOR ANINHADO ')

compras = [['arroz', 'feijão', 'macarrão'], ['carne', 'frngo', 'ovo'], ['leite', 'iorgute']]

print('IMPRIMINDO  LISTA')
for i in compras:
    print(i)

print('Imprimindo cada item de cada lista')
for i in compras:
    for item in i:
        print(item)
print('#' * 25)

print('LOOP FOR COM RANGE')
for i in range(0,10):
    print(i)

print('#' * 25)
print('CONTAGEM REGRESSIVA')
for i in range(0,10):
    print(10 - i)