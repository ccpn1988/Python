# 057 - LER O SEXO E SO ACEITAR M ou F
# CASO ESTEJA ERRADO PEÇA NOVAMENTE ATE TER O VALOR CORRETO.

sexo = str(input('Informe o sexo [M]/[F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input(f'O sexo {sexo} informado é inválido, informe o sexo [M]/[F]: '))
if sexo in 'Mm':
    print(f'Sexo MASCULINO, digitado corretamente. ')
elif sexo in 'Ff':
    print(f'Sexo FEMININO digitado corretamente.')