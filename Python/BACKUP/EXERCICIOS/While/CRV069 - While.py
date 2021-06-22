# 069 - LER IDADE E O SEXO DAS PESSOAS

tot18 = 0
m = 0
f = 0
fem20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
        if sexo == 'M':
            m += 1
        if sexo == 'F' and idade < 20:
            fem20 +=1
    while sexo not in 'FM':
        print(f'Sexo invalido....', end=' ')
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]

    flag = ' '
    while flag not in 'SN':
        flag = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if flag == 'N':
        break
print(f'Foram informados {m} homens')
print(f'Foram informados {tot18} pessoas com mais de 18 anos')
print(f'Foram informados {fem20} mulheres com menos de 20 anos')
print('Encerrando...')

#while True:
#    idade = int(input('Digite sua idade: '))
#    sexo = ' '
#    while sexo not in 'MF':
#        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
#    if idade >= 18:
#        tot18 += 1
#    if sexo == 'M':
#        m += 1
#    if sexo == 'F' and idade > 20:
#        fem20 += 1
#    flag = ' '
#    while flag not in 'SN':
#        flag = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
#    if flag == 'N':
#        break
# print(f'Foram informados {m} homens')
# print(f'Foram informados {tot18} pessoas com mais de 18 anos')
# print(f'Foram informados {fem20} mulheres com menos de 20 anos')
# print('Encerrando...')
