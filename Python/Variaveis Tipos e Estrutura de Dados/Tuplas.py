#!/usr/bin/env python
# coding: utf-8

# ## TUPLAS - USADO QUANDO O CONTEUDO NAO DEVE SER ALTERADO

# In[1]:


# Criando uma tupla -> criado com parenteses
tupla1 = ('Geografia', 23, "Elefantes")


# In[2]:


tupla1


# In[1]:


# Tuplas não suportam append
tupla1.append('Caio')


# In[1]:


# Tuplas nao suportam delete de um item
del tupla1[23]


# In[3]:


# Tuplas podem ter 1 item
tupla1 = ('Chocolate')


# In[4]:


tupla1


# In[5]:


# Criando uma tupla
tupla1 = ('Geografia', 23, "Elefantes")


# In[6]:


tupla1


# In[1]:


# Criando uma tupla
tupla1 = ('Geografia', 23, "Elefantes")


# In[7]:


# Aceita o uso de indice
tupla1[0]


# In[10]:


# Slicing da mesma forma que é feito com listas
tupla1[1:]


# In[12]:


tupla1.index('Elefantes')


# In[13]:


del tupla1


# In[14]:


# Criando uma tupla
t2 = ('Caio', 25 , 'Gabi')


# In[15]:


# Usando a função list() para converter tupla para list -> lista = list(tupla)
lista_t2 = list(t2)


# In[16]:


lista_t2


# In[17]:


lista_t2.append('D')


# In[18]:


lista_t2


# In[19]:


# Usando a função tuple() para converter lista para tupla -> tupla = tuple(lista)
t2 = tuple(lista_t2)


# In[20]:


t2

