nome = input('Informe o nome do colaborador: ')
salario = float(input('Informe o salario mensal do colaborador: '))
percent_aumento = 0.65

aumento = salario * percent_aumento
novo_salario = aumento + salario

print('O colaborador e:', nome)
print('O salario atual do:' + nome + ' e:', salario)
print('O percentual de aumento do: ' + nome + ' e:', percent_aumento)
print('O valor acordado para aumento do: ' + nome + ' e:', aumento)
print('O novo salario do: ' + nome + ' e:', novo_salario)

