# continue = pula para proxima
# break = termina o laço

texto = 'BACKUP'
nova_string = ' '

for letra in texto:
    if texto == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)