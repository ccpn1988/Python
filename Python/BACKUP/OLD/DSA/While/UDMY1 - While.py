# While
# Continue = sai do loop e volta p inicio
# break = sai do loop

pessoas = []
x = 0
while x < 4:
    nome = str(input('Digite seu nome: '))
    pessoas.append(nome)
    x += 1
print(pessoas)


while True:
    nome = str(input('Digite seu nome: ')).upper()
    if nome == 'joao':
        # SAIA DO LOOP E VOLTA P INICIO
        continue
    pessoas.append(nome)
print(pessoas)


