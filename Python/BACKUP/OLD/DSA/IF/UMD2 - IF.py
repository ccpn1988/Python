nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

menor_idade = 18
maior_idade = 35

if idade >= menor_idade and idade <= maior_idade:
    print(f'{nome} pode adquirir emprestimos')
else:
    print(f'{nome} não pode adquirir emprestimos..')