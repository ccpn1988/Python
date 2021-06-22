nome = str(input('Digite seu nome... ')) .title()
minha_idade = 32
print(f'{nome} tem {minha_idade} anos')

taxa_usd = 5.88
carteira = 1578
dolar = carteira / taxa_usd
print(f'Você tinha R$ {carteira} com a cotação do USD em USD {taxa_usd}, agora temos {dolar:.2f} dolares')


# DECLARANDO MULTIPLAS VARIAVEIS POR JUSTAPOSIÇÂO

nome = "Maria"
idade = 32
sexo = 'F'

nome,idade,sexo = 'Maria', 32, 'F'

print(nome,idade,sexo)
