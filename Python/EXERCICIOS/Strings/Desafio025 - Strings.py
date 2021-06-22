# VALIDE SE EXISTE O SOBRENOME SILVA NO NOME INSERIDO

nome = str(input('Informe seu nome completo... ')).strip()
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')
