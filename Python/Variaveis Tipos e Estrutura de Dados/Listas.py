#!/usr/bin/env python
# coding: utf-8

# ## LISTAS

# In[5]:


# criando uma lista de 1 elemento
listadomercado = ["ovos, farinha, leite, maças"]


# ## LISTAS

# In[6]:


# Imprimindo uma lista
print(listadomercado)


# In[16]:


# Criando outra Lista com 4 elementos
listadomercado2 = ["ovos", "farinha", "leite", "maças"]


# In[17]:


print(listadomercado2)


# In[19]:


# Imprimindo primeiro item da lista
listadomercado[0]


# In[20]:


listadomercado2[0]


# In[14]:


# Criando Lista
lista3 = [12, 100, 'Universidade']


# In[15]:


# Imprimindo
print(lista3)


# In[22]:


# Atribuindo valores da lista a uma variavel.
item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]


# In[23]:


# Imprimindo as variaveis
print(item1)
print(item2)
print(item3)


# ## Atualizando listas
#

# In[24]:


# Imprimindo item da lista
listadomercado2[0]


# In[25]:


# Atualizando item da lista
listadomercado2[0] = 'chocolate'


# In[26]:


# Imprimindo item alterado da lista
listadomercado2[0]


# ## Deletando um item da lista

# In[27]:


# Out of Index, não é possivel deletar um item que não exista na lista
del listadomercado2[4]


# In[28]:


# Deletando item da lista
del listadomercado2[0]


# In[29]:


# Imprimindo lista após delete
listadomercado2


# ## Listas Aninhadas

# In[34]:


# Criando uma lista de lista = listas dentro de outra lista
listas =  [[1,2,3], [10,15,14], [10,1,8,7,2,3]]


# In[35]:


# Imprimindo listas
listas


# In[37]:


# Atribuindo um item da lista a uma variavel.
a = listas[0]


# In[39]:


# Imprimindo variavel atribuida a lisa de indice 0
a


# In[40]:


# Atribuindo 1 valor da lista para outra variável.
b = a[0]


# In[41]:


# Imprimindo item atribuido
b


# In[42]:


# Atribuindo item a uma variavel
list1 = listas[1]


# In[43]:


# Imprimindo conteudo da varivael
list1


# In[47]:


valor_1_0 = list1[0]


# In[48]:


valor_1_0


# In[49]:


list1[0]


# In[50]:


valor_1_2 = list1[2]


# In[51]:


valor_1_2


# In[52]:


valor_1_3 = list1[1]


# In[53]:


valor_1_3


# ## Operações com Listas

# In[54]:


# Criando uma lista aninhada(Lista de Listas)
listas = [[1,2,3], [10,15,14],[10.1,8.7,2.3]]


# In[55]:


# Imprimindo Lista
listas


# In[56]:


# Atribuindo a variavel 'a' o primeiro valor da primeira lista
a = lista[0][0]


# In[57]:


# Imprimindo valor da varavel 'a'
a


# In[58]:


# Adicionando conteudo 14 (indice 2) d0 2 bloco (indice '1') da lista
b = listas[1][2]


# In[59]:


# Imprimindo variavel b
b


# In[60]:


c = listas[0][2] +10


# In[61]:


# Imprimindo item alterado da lista
c


# In[62]:


d = 10


# In[63]:


e = d * listas[2][0]


# In[64]:


e


# ## Concatenando listas

# In[65]:


lista_s1 = [34,32,56]


# In[66]:


lista_s1


# In[67]:


lista_s2 = [21,90,51]


# In[68]:


lista_s2


# In[69]:


# Concatenando listas
lista_total = lista_s1 + lista_s2


# In[70]:


# Imprimindo lista concatenada
lista_total


# ## Operador IN

# In[71]:


# Criando Lista
lista_teste_op = [100, 2, -5, 3.4]


# In[72]:


# Verificando se o valor pertence a lista
print(10 in lista_teste_op)


# In[73]:


print(100 in lista_teste_op)


# ## Funções Built-IN

# In[74]:


# Tamanho da Lista
len(lista_teste_op)


# In[75]:


# Valor máximo da lista
max(lista_teste_op)


# In[76]:


# Valor minimo da lista
min(lista_teste_op)


# In[77]:


# Criando uma lista
listadomercado2 = ["ovos", "farinha", "leite", "macas"]


# In[78]:


# Adicionando item a lista
listadomercado2.append("carne")


# In[79]:


listadomercado2


# In[87]:


# Contando a quantidade o mesmo registro
listadomercado2.count("carne")


# In[88]:


# Criando uma lista vazia
a = []


# In[89]:


# Validando o tipo da lista
type(a)


# In[90]:


# Inserindo registros
a.append(10)


# In[91]:


a


# In[92]:


a.append(50)


# In[93]:


print(a)


# In[94]:


# Criando Nova Lista
old_list = [1,2,5,10]


# In[97]:


# Criando Lista Vazia
new_list = []


# In[98]:


# Copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)


# In[100]:


new_list


# In[101]:


c = [20,30]


# In[102]:


c.append(50)


# In[103]:


c.append(70)


# In[104]:


c


# In[105]:


c.count(20)


# In[107]:


# Adiicionando lista extendida
cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print(cidades)


# In[109]:


#
cidades.index('Salvador')


# In[110]:


cidade.index('Rio de Janeiro')


# In[111]:


# Insere dados lista(indice,novo)
cidades.insert(2,100)


# In[112]:


cidades


# In[113]:


# Removendo item da lista
cidades.remove(100)


# In[114]:


cidades


# In[115]:


# Reverte a lista
cidades.reverse()


# In[116]:


cidades


# In[117]:


x = [3,4,2,1]


# In[118]:


# Ordenando a lista
x.sort()


# In[119]:


x

