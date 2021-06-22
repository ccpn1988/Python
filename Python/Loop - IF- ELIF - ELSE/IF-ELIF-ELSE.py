#!/usr/bin/env python
# coding: utf-8

# ## CONDICIONAL IF

# In[ ]:


# Condicional IF
if 5 > 2:
    print("Python Funcional")


# In[ ]:


# Statement if ..... Else
if 5 < 2:
    print("Python Funcional !!!")
else:
    print("Algo está errado !!!")


# In[ ]:


6 > 3


# In[ ]:


3 > 7 


# In[ ]:


4 < 8 


# In[ ]:


4 >= 4


# In[ ]:


if 5 == 5:
    print("Testando Python !!!")


# In[ ]:


if 5 == 6:
    print("Testando Python !!!")
elif 5 != 5:
    print("Tem algo estranho !!!")
else:
    print("Nada Mudou !!!")


# ## Condicionais Aninhados

# In[ ]:


idade = 18
if idade > 17:
    print("VocÊ pode dirigir")
    


# In[ ]:


Nome = 'Bob' 
idade = 15
if idade > 13:
    print('Ok Bob, você pode entar !!!')
else:
    print("Bob, infelizemente vc nao tem idade suficiente")


# In[ ]:


Nome = "Bob"
idade = 13
if idade < 13:
  if Nome == "Bob":
    print('Ok Bob, você pode entar !!!')
else:
    print("Bob, infelizemente vc nao tem idade suficiente")


# In[ ]:


Nome = "Bob"
idade = 13
if Nome == "Bob" and idade >= 13:
    print("Entre Bob !!!")
else:
    print("Bob, infelizemente vc nao tem idade suficiente")


# In[ ]:


Nome = "Bob"
idade = 13
if (idade >= 13) or (Nome == "Bob"):
    print("Pode entrar!")


# ## Elif

# In[ ]:


dia = "Terça"
if dia == 'Segunda':
    print("Hoje fara sol !!!")
else :
    print("Hoje vai chover !!!")


# In[ ]:


if dia == 'Segunda':
    print('Hoje fara sol !!!!')
elif dia == "Terça":
    print("Hoje vai chover")
else:
    print("Sem previsão do tempo para o dia selecionado")


# ## Operadores Logicos

# In[ ]:


idade = 18
nome = "Bob"
if idade > 17:
    print("Você pode dirigir !!")


# In[ ]:


idade = 18
if idade >= 18 and nome == "Bob":
    print("Autorizado !!! ")


# In[5]:


## Usando mais de uma condição na clausula IF

disciplina = input("Digite o nome da disciplina : ")
nota_final = input("Digite a nota final (entre 0 e 100): ")

if disciplina == 'Geografia' and nota_final >= '50':
     print('Você foi aprovado')
elif disciplina == 'Matematica' or nota_final <= '70':
    print('Você foi aprovado')
elif disciplina == 'Portugues ' and nota_final >= '60':
    print('Você foi aprovado')
else:
    print("Lamento, acho que vc precisa estudar mais !!!! ")


# In[12]:


## Usando mais de uma condição na clausula IF e introduzindo Placeholders.....

disciplina = input("Digite o nome da disciplina : ")
nota_final = input("Digite a nota final (entre 0 e 100): ")
semestre = input("Digite o semestre (1 a 4) : ")

# Faz a conversão do valor imputado na variavel semestre para int.
if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1:
    print("Você foi aprovado em %s com média final %r!!!" %(disciplina, nota_final))
#Placeholders = "string %letra" -> %(variaveis, variaveis1) 
else:
    print("burro que só uma porra !!!")


# In[ ]:


## Condicionais Aninhados


# In[ ]:


## Condicionais Aninhados


# In[ ]:


## Condicionais Aninhados

