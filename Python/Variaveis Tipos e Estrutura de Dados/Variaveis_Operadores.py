#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[3]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Variáveis e Operadores 

# In[4]:


# Atribuindo o valor 1 à variável var_teste
var_teste = 1


# In[5]:


# Imprimindo o valor da variável
var_teste


# In[ ]:


# Imprimindo o valor da variável
print(var_teste)


# In[ ]:


# Não podemos utilizar uma variável que não foi definida. Veja a mensagem de erro.
my_var


# In[ ]:


var_teste = 2


# In[ ]:


var_teste


# In[ ]:


type(var_teste)


# In[ ]:


var_teste = 9.5


# In[ ]:


type(var_teste)


# In[ ]:


x = 1


# In[ ]:


x


# ## Declaração Múltipla

# In[6]:


pessoa1, pessoa2, pessoa3 = "Maria", "José", "Tobias"


# In[7]:


pessoa1


# In[8]:


pessoa2


# In[9]:


pessoa3


# In[10]:


fruta1 = fruta2 = fruta3 = "Laranja"


# In[11]:


fruta1


# In[12]:


fruta2


# In[ ]:


# Fique atento!!! Python é case-sensitive. Criamos a variável fruta2, mas não a variável Fruta2.
# Letras maiúsculas e minúsculas tem diferença no nome da variável.
Fruta2


# ## Pode-se usar letras, números e underline (mas não se pode começar com números)

# In[ ]:


x1 = 50


# In[ ]:


x1


# In[ ]:


# Mensagem de erro, pois o Python não permite nomes de variáveis que iniciem com números
1x = 50


# ## Não se pode usar palavras reservadas como nome de variável
# 
# ## False      
# ## class      
# ## finally    
# ## is         
# ## return
# ## None       
# ## continue   
# ## for        
# ## lambda     
# ## try
# ## True       
# ## def        
# ## from       
# ## nonlocal   
# ## while
# ## and        
# ## del        
# ## global     
# ## not        
# ## with
# ## as         
# ## elif       
# ## if         
# ## or         
# ## yield
# ## assert     
# ## else       
# ## import     
# ## pass
# ## break      
# ## except     
# ## in         
# ## raise

# In[ ]:


# Não podemos usar palavras reservadas como nome de variável
break = 1


# ## Variáveis atribuídas a outras variáveis e ordem dos operadores

# In[ ]:


largura = 2


# In[ ]:


altura = 4


# In[ ]:


area = largura * altura


# In[ ]:


area


# In[ ]:


perimetro = 2 * largura + 2 * altura


# In[ ]:


perimetro


# In[ ]:


# A ordem dos operadores é a mesma seguida na Matemática
perimetro = 2 * (largura + 2)  * altura


# In[ ]:


perimetro


# ## Operações com variáveis

# In[ ]:


idade1 = 25


# In[ ]:


idade2 = 35


# In[ ]:


idade1 + idade2


# In[ ]:


idade2 - idade1


# In[ ]:


idade2 * idade1


# In[ ]:


idade2 / idade1


# In[ ]:


idade2 % idade1


# ## Concatenação de Variáveis

# In[ ]:


nome = "Steve"


# In[ ]:


sobrenome = "Jobs"


# In[ ]:


fullName = nome + " " + sobrenome


# In[ ]:


fullName


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
