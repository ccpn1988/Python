#!/usr/bin/env python
# coding: utf-8

# ## STRINGS

# # INDICES COMEÇAM COM ZERO ( 0 )

# In[1]:


texto = "Python e Analise de Dados"


# In[2]:


texto[0]


# In[3]:


texto[1]


# In[4]:


texto[2]


# In[5]:


texto[3]


# In[6]:


texto[4]


# In[7]:


texto[5]


# ## CRIANDO UMA STRING - Pode usar aspas simples ou duplas

# In[8]:


# uma unica palavra
"a"


# In[9]:


# uma frase
"Sociedade Esportiva Palmeiras"


# In[10]:


# uma frase
"Criando uma frase em Python"


# In[12]:


# Podemos usar aspas simples
'Podemos usar aspas simples ou duplas, para criar uma string em Python'


# In[13]:


# Combinando as simples e duplas
"Testando Strings em 'Python'"


# ## IMPRIMINDO UMA STRING

# In[14]:


print('Testando String em Python')


# In[15]:


print ('Testando \nstrings \nem \nPython')


#  ## INDEXANDO UMA STRING

# In[19]:


# Atribuindo uma string
s = "Data Science Academy"


# In[20]:


print(s)


# In[21]:


# O primeiro elemento da String
s[0]


# ## Podemos usar um : para executar um slicing que faz a leitura de tudo até um ponto designado. Por exemplo

# In[24]:


# A partir do Indice 1, pegando todo o conteúdo.
s[1:]


# In[22]:


# Retorna tudo ate a posição 3
s[:3]


# In[25]:


# A string original permanece inalterada
s


# In[26]:


s[:]


# In[23]:


# Pode usar indexação negativa e ler de trás para frente
s[-1]


# In[27]:


# Retornar tudo, exceto a ultima letra
s[:-1]


# In[ ]:


Nós também podemos usar a notação de índice e fatiar a string em pedaços específicos (o padrão é 1). Por exemplo, podemos usar dois pontos duas vezes em uma linha e, em seguida, um número que especifica a frequência para retornar elementos. 
Por exemplo


# In[30]:


# Retorna todos os caracteres, pulando 1 posição
s[::1]


# In[31]:


# Retorna todos os caracteres, pulando 2 posições
s[::2]


# In[32]:


# Retorna todos os caracteres, pulando 2 posições
s[::-1]


# ## Propriedade de String

# In[35]:


s


# In[36]:


# Alterando um caractere
s[0] = 'x'


# In[37]:


# Concatenação strings
s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados'


# In[38]:


# Armazenando o valor em uma stringv
s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados'


# In[39]:


print(s)


# In[40]:


# Usando simbolo de multiplicação para criar repetição!
letra = 'w'


# In[41]:


letra * 3


# ## Função Built-in de Strings

# In[43]:


s


# In[44]:


# Upper - Case
s.upper()


# In[45]:


# lower - Case
s.lower()


# In[46]:


# Dividir uma sprint por espaços em branco
s.split()


# In[49]:


# Dividir a string por um elemento especifico
s.split('a')


# ## Funções Strings

# In[55]:


s = 'seja bem vindo ao universo python'


# In[56]:


# Deixa em maiusculo o primeiro caractere
s.capitalize()


# # Pega a posição da string definida
# s.count('a')

# In[58]:


# Pesquisa o caractere definido
s.find('p')


# In[59]:


# Verifica se a String contem caractere minusculo
s.islower()


# In[60]:


# Verifica se a string é espaço
s.isspace()


# In[62]:


# Verifica se a string encerra com a letra O
s.endswith('o')


# ## Comparando String

# In[63]:


print("Python" == 'R')


# In[64]:


print("Python" == 'Python')

