#!/usr/bin/env python
# coding: utf-8

# # Aula 8 - pandas
# 
# Na aula de hoje, vamos explorar os seguintes tópicos em Python:
# 
# - 1) Introdução ao Pandas
# - 2) Conceitos de Dataframe e Series
# - 3) Axis e slicing: uso de loc/iloc
# - 4) Criação e manipulação de DF e SS a partir de dicionário, listas e arrays
# - 5) Filtragem de dados e parâmetro inplace
# - 6) Leitura de dados (read_csv, read_excel, read_clipboard)
# _______
# 
# ### Objetivos
# 
# Apresentar o pandas, frisando sua importância para o processamento de dados e em data science. Apresentar seus principais conceitos (Series, DataFrame) e funcionalidades (leitura de arquivo, filtros, seleção, apply, escrita de arquivos, etc.)
# 
# ### Habilidades a serem desenvolvidas nessa aula
# 
# Ao final da aula o aluno deve:
# 
# - Conhecer o pandas, suas vantagens e principais usos;
# - Saber como ler um arquivo com o pandas (csv, excel, etc.), criando DataFrames;
# - Entender o conceito de Series e como elas são construídas;
# - Entender o conceito de DataFrame em termos das Series;
# - Saber como trabalhar com DataFrames para o processamento de dados:
#     - Seleções: uso de loc/iloc;
#     - Filtros;
#     - Criação de novas colunas.
# - Saber como ler e escrever de/em um arquivo com o pandas (csv, excel, etc.).

# ____
# ____
# ____

# ## 1) Pandas
# 
# O pandas é uma das bibliotecas mais usadas em data science.
# 
# Seu objetivo é a **leitura, processamento e manipulação de dados** na forma de tabelas chamadas de **"DataFrame"**
# 
# <img src="pandas-data-structure.svg"  style="width: 700px" >
# 
# Antes de conhecer o Pandas, vamos ler o arquivo "alunos.csv", da forma como aprendemos na aula de arquivos

# In[127]:


import csv

f = open("alunos.csv", "r", encoding="utf-8")

leitor = csv.reader(f, delimiter=';', lineterminator='\n')

planilha = []

for linha in leitor:
    planilha.append(linha)
    
f.close()

planilha


# Como fizemos na aula, uma vez lido o arquivo, é possível processá-lo de diversas maneiras.
# 
# Por exemplo, para obter **a primeira coluna**, isto é, os nomes, fazemos:

# In[128]:


[item[1] for item in planilha if item[1]!='Nome']


# Agora, vamos usar o Pandas e aprender uma forma muito mais fácil de processar dados!

# Existem diversas formas de instalar o pandas. A mais simples é instalar o pacote Anaconda (https://www.anaconda.com/distribution/) que já vem com o Python e diversas bibliotecas científicas e ciência de dados instaladas.
# 
# Outra forma, caso você já tenha o python instalado mas não o pandas, é o utilizar o gerenciador e pacotes pip, através do comando no seu **terminal**:
# 
# `$ pip install pandas`
# 
# ou dentro do jupyter
# 
# `!pip install pandas`

# In[129]:


# importando a biblioteca
import pandas as pd

# lendo o arquivo
tabela = pd.read_csv("alunos.csv", sep=";")

tabela


# ### Acessando elementos

# Podemos **acessar os valores nas colunas** pelo nome delas:

# In[130]:


tabela['Nome']


# In[131]:


tabela.loc[tabela['Frequencia']==20,'Nome']


# In[132]:


# acessar coluna "Nome" diretamente
tabela["Nome"]
tabela.Nome


# In[133]:


# acessar coluna "Nome" através de uma variável
nome_da_coluna = "Nome"

type(tabela[nome_da_coluna])


# Se quisermos obter uma lista propriamente com os valores na coluna, usamos o método `tolist()`:

# In[134]:


tabela["Nome"].tolist()


# Dá pra **selecionar apenas algumas colunas** do dataframe (ou seja, criando um sub-dataframe):

# In[135]:


# pegando apenas a coluna "Nome" e resultado da "Prova_1"
tabela[["Nome", "Prova_1"]]


# ### Acessando elementos

# Podemos utilizar o `.loc[indice_linhas, nome_colunas]` para acessar determinas colunas e as linhas através dos índices e nomes das colunas.

# In[136]:


# selecionar todas as linhas das colunas ['Nome','Prova_1']
tabela.loc[:, ["Nome", "Prova_1"]]


# In[137]:


# selecionar linhas 3 à 5 das colunas ['Nome','Prova_1']
tabela.loc[3:5, ["Nome", "Prova_1"]]


# In[138]:


# selecionar linhas 3,5,9 das colunas ['Nome','Prova_1']
tabela.loc[[3,5,9], ["Nome", "Prova_1"]]


# In[139]:


# selecionar as linhas das colunas Prova_1 até Prova_4
tabela.loc[:, 'Prova_1':'Prova_4']


# selecionar apenas uma linha de uma coluna

# In[140]:


tabela.loc[9, "Nome"]


# É possível **alterar valores** da tabela. Para isso, primeiro localizamos o valor a ser alterado com o **.loc**, passando a linha e coluna correspondente, e depois atribuímos o novo valor

# In[141]:


tabela.loc[10, "Nome"] = "Joãozinho"
tabela.loc[10, "Frequencia"] = 100


# In[142]:


tabela


# In[143]:


tabela = tabela.set_index('Nome')
tabela


# Vamos tentar selecionar as linhas 3 à 5 das colunas ['Prova_1','Prova_2'] como fizemos anteriormente

# In[144]:


tabela.loc[3:5, ['Prova_1','Prova_2']]


# O que aconteceu? <br>
# O `.loc` faz o slice considerando o index da matriz e agora o index é o nome dos alunos. 

# In[ ]:


tabela.loc['Francisco Cunha':'Juliana Arruda', ['Prova_1','Prova_2']]


# Para resetar o index e voltarmos a ter os valores originais:

# In[ ]:


tabela.reset_index(inplace=True)
tabela


# Repare que quando utilizamos o `inplace=True` como um argumento do método nós não precisamos referenciar o dataframe. <br>
# Nós podemos utilizar o `inplace=True` em vários métodos do pandas.

# ### Seleção através das posições das linhas e colunas
# Outra forma de acessarmos dados é através do `.iloc[número_linhas, número_colunas]` utilizando as posições das linhas e colunas

# In[ ]:


# seleciona uma linha de uma coluna
tabela.iloc[10, 1]


# In[ ]:


# seleciona todas as colunas de uma linha
tabela.iloc[10, :]


# In[ ]:


# seleciona um conjunto de linhas sequenciais de um conjunto de colunas sequenciais
tabela.iloc[3:5, 1:5]


# In[ ]:


# seleciona um conjunto de linhas sequenciais de um conjunto de colunas não sequenciais
tabela.iloc[3:5, [1,5]]


# In[ ]:


tabela[0] = 0


# ### Diferença entre .loc e .iloc
# O .loc irá trazer o dado utilizando o índice, não importando se o índice não está ordenado. Já o .iloc irá respeitar a ordem atual dos dados

# In[ ]:


tabela_copy = tabela.copy()


# In[ ]:


# vamos bagunçar o índice do df chamado tabela
tabela_copy.index = sorted(tabela.index.values, reverse=True)
tabela_copy.head()


# In[ ]:


# traz o índice
tabela_copy.loc[[3,6],:]


# In[ ]:


# iloc traz a linha
tabela_copy.iloc[[3,6],:]


# ### Criar novas colunas

# **Criando uma coluna nova**, com todas as linhas preenchidas com o mesmo valor

# In[ ]:


# cria coluna com valores 1
tabela["cheia_de_um"] = 1


# In[ ]:


# cria coluna com string
tabela["aaaa"] = "a"


# In[ ]:


# cria coluna vazia
tabela["vazio"] = ""


# In[ ]:


tabela


# Também é possível **criar uma linha nova** atribuindo valores para todas as colunas:

# In[ ]:


tabela.loc[10, :] = [1245245, "Joãozinho", 100, 10, 4, 6, 7, "bbb", 2, "cheio"]

tabela


# Se você usar o index de uma linha que já existe irá substituí-la.

# Podemos fazer **operações entre os valores das colunas**, e criar com isso novas colunas!

# In[ ]:


# calculando a média usando as colunas Prova_1, Prova_2, Prova_3 e Prova_4
tabela["média"] = (tabela["Prova_1"] + tabela["Prova_2"] + 
                   tabela["Prova_3"] + tabela["Prova_4"])/4


# Também há alguns métodos prontos que facilitam a utilização:

# In[ ]:


# calculando a media com o método .mean(axis=1)
tabela["media_2"] = tabela[["Prova_1", "Prova_2", "Prova_3", "Prova_4"]].mean(axis=1)

tabela


# Naturalmente, o resultado é o mesmo!

# ### Métodos:
# 
# O Pandas possui diversos métodos que podem ser utilizados nessa estrutura.
# Abaixo estão alguns métodos que essa estrutura de dados possui e facilitam alguns cálculos e análises:
#  
# 
# | Método      | Descrição     |
# | ----------- | -----------   |
# | sum         | soma          |
# | mean        | média         |
# | std         | desvio padrão |
# | mode        | moda          |
# | max         | valor máximo  |
# | min         | valor mínimo  |
# | idxmax      | primeiro índice com valor máximo |
# | idxmin      | primeiro índice com valor mínimo |
# | value_counts | contagem de valores |
# | describe    | estatísticas básicas |
# 
# 
# Na próxima aula veremos mais alguns.
# 

# In[ ]:


# calculando o valor máx de cada aluno
tabela[["Prova_1", "Prova_2", "Prova_3", "Prova_4"]].max(axis=1)


# In[ ]:


# calculando o valor máx de cada prova
tabela[["Prova_1", "Prova_2", "Prova_3", "Prova_4"]].max(axis=0)


# ### Filtros

# Podemos **fazer filtros** muito facilmente
# 
# Basta explicitarmos **condições sobre os valores das colunas**, e utilizar isso como indexador do dataframe!

# In[ ]:


# retorna o sub-dataframe que contém valores maiores que 7 na coluna "média"
# ou seja, é um filtro que utiliza a coluna "média"!

tabela[tabela["média"] > 7]


# Se quisermos fazer filtros mais complexos (filtros compostos, em mais de uma coluna), podemos fazer **conjunções entre filtros**, utilizando os **operadores lógicos de conjunção**.
# 
# Obs.: temos os seguintes operadores lógicos:
# 
# - &     - corresponde ao "and"
# - |     - corresponde ao "or"
# - ~     - corresponde ao "not"

# In[ ]:


# filtar tabela para média > 7 e frequencia >= 20
tabela[(tabela["média"] > 7) & (tabela["Frequencia"] >= 20)]


# In[ ]:


# filtar tabela para média > 7 e frequencia >= 20
tabela[(tabela["média"] > 7) | (tabela["Frequencia"] >= 20)]


# In[ ]:


# pegando somente a coluna "média" dos alunos que tiveram nota igual na prova 1 e na prova 4
tabela[tabela["Prova_4"] == tabela["Prova_1"]]["média"]


# In[ ]:


# calculando a média de todos os alunos que tiveram nota igual na prova 1 e na prova 4
tabela[tabela["Prova_4"] == tabela["Prova_1"]]["média"].mean()


# In[ ]:


# Podemos criar um novo df diretamento do filtro
prova_4 = tabela[tabela['Prova_4']>=7]
prova_4


# E também é bem fácil salvar um dataframe de volta pra CSV ou pro Excel. 

# In[ ]:


# salvando dados em csv com o método .to_csv()
tabela.to_csv("tabela_processada2.csv", sep=";")


# Para salvar esses dados em excel é preciso instalar mais uma biblioteca: a `openpyxl`. Caso você não a tenha escreva o comando seguinte em uma célula de código: <br>
# ` !pip install openpyxl `
# <br>
# 

# In[ ]:


# salvando dados em excel com o método .to_excel()
tabela.to_excel("tabela_processada.xlsx")


# Agora que entendemos na prática como usar o Pandas, vamos nos aprofundar um pouco mais em sua estrutura!

# ### Outra forma de filtrar: `.query()`

# In[ ]:


prova_4 = tabela.query('Prova_4 >= 7 and Prova_3 >= 7')
prova_4


# ## Series
# O objeto fundamental do Pandas são as **Series**.
# 
# As Series são as **colunas das tabelas**, que são originadas de um array unidimensional capaz de guardar qualquer tipo de dado (integers, strings, floating point numbers, Python objects, etc.). E como as listas, as series podem conter dados de vários tipo.

# In[ ]:


tabela


# Visual de uma series:

# In[ ]:


tabela.cheia_de_um


# Tipo de uma series

# In[ ]:


type(tabela.cheia_de_um)


# Como pudemos observar a series pode ter elementos de diferentes tipos. Na primeira posição temos um float enquanto na última temos uma string.

# In[ ]:


type(tabela.cheia_de_um[0])


# In[ ]:


type(tabela.cheia_de_um[10])


# A diferença é que a series possui um **índice associado**, permitindo o acesso aos conteúdos dessa estrutura por ele, como um dicionário. Para entender mais sobre como trabalhar como séries, temos um conteúdo anexado no final desse notebook que você pode olhar.

# Agora que entendemos a componente fundamental do Pandas, as Séries, vamos falar um pouco mais sobre o **DataFrame**

# ### Estrutura do df
# O DataFrame é uma estrutura que se assemelha a uma tabela/planilha, como vimos acima.
# 
# Por debaixo dos panos, o dataframe é representado por um dicionário em que a **chave** é o **nome da coluna** e os **valores** são as **Series** (todas com mesmo índice).

# ### Criação de df a partir de dicionários

# Assim, podemos **criar um dataframe a partir de um dicionario**, usando a função `pd.DataFrame()` 

# In[ ]:


cadastro = {"nomes" : ["André", "Mariazinha"],
                "idade" : [22, 25],
                "cidade" : ["Mauá", "Santo André"],
                "filhos": [0, 0],
                "altura" : [1.80, 1.65]}

cadastro


# In[ ]:


# criando um dataframe a partir de um dicionario
df = pd.DataFrame(cadastro)
df


# ## Outros conteúdos

# ### Criar Series a partir de listas
# 
# Podemos criar uma series **a partir de uma lista**, usando a função do pandas `pd.Series()`: 

# In[ ]:


# definindo uma série com valores e indices
indices = ["a", "b", "c", "d"]
lista = [10, 20, 30, 40]

serie = pd.Series(data = lista, index = indices)

serie


# Podemos acessar o elemento 30, que está associado ao índice c:

# In[ ]:


serie['c']


# Para retornar todos os índices podemos utilizar o método `series.index`

# In[ ]:


serie.index


# E para acessar os valores podemos utilizar o atributo `series.values`
# 

# In[ ]:


serie.values


# ### Utilizando filtros em Series
# Podemos aplicar filtros para selecionar apenas os elementos que satisfaçam determinada condição.
# No exemplo abaixo, iremos selecionar apenas os elementos que sejam maiores que 15:
# 

# In[ ]:


serie[serie > 15] 


# Note que `serie > 15` nos retorna uma series com elementos `True` e `False`, caso os elementos da serie satisfaçam a condição. Ao utilizar esse comando dentro dos colchetes, `serie[serie > 15]`, estamos selecionado apenas os elementos que satisfazem a condição.

# 
# ### Criar Series a partir de dicionários
# Também podemos **criar uma série a partir de um dicionário**, e os índices e valores são automaticamente capturados:

# In[ ]:


# criando uma série a partir de um dicionario
dic2 = {"nome": "André", 
        "idade" : 23}

pd.Series(dic2)


# ### Criar dicionários a partir de Series
# O inverso também é possível:

# In[ ]:


dicionario = dict(serie)

dicionario


# ### Criar dataframe a partir de listas

# In[ ]:


# Considere a seguinte lista
age = [['Artur', 95.5, "M"], ['Vera', 79.7, "F"],
       ['Mônica', 85.1, "F"], ['Toni', 75.4, "M"]]
  
# Cria um pandas dataframe passando a lista e, se quiser, o nome das colunas
pd.DataFrame(age, columns=['Npme', 'Pontos', 'Sexo'])


# ### Criar dataframe a partir de array

# In[ ]:


import numpy as np

# Considere o seguinte array:
my_array = np.random.randint(1, 10, 18)

# Cria um pandas dataframe passando o array e, se quiser, o nome das colunas
pd.DataFrame(my_array.reshape(-1,3), columns=['col_1','col_2','col_3'])


# ## Exercícios

# 1 - Realize os passos seguintes utilizando o mesmo dataset do íris da aula anterior ('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').
# 
# a. Use o pandas para ler o arquivo como um dataframe. Obs: precisa ler o dataframe sem que a primeira linha corresponda ao nome das colunas.

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('iris.data', header=None)
df


# b. Sabendo que as colunas correspondem, nessa ordem, a: 
#     1. sepal length (cm)
#     2. sepal width (cm)
#     3. petal length (cm)
#     4. petal width (cm)
#     5. class: <br>
#         - Iris Setosa <br>
#         - Iris Versicolor <br>
#         - Iris Virginica <br>
# leia novamente o arquivo passando o nome das colunas como argumento.

# In[3]:


df.columns=['sepal_length','sepal_width','petal_length','petal_width','Class']
df


# c. Calcule a média de cada coluna numérica para cada um dos tipos de íris indicados na coluna "class" sem utilizar métodos que não foram ensinados na aula de hoje. Utilize o loop for para reduzir quantidade de linhas. <br>
# Existe diferença entre elas?

# In[4]:


df['Class'].unique()


# In[5]:


media_Iris_Setosa=df[df['Class']=='Iris-setosa'].mean()
media_Iris_Setosa


# In[6]:


media_Iris_Setosa.sepal_length


# In[7]:


media_Iris_Versicolor=df[df['Class']=='Iris-versicolor'].mean()
media_Iris_Versicolor


# In[8]:


media_Iris_Virginica=df[df['Class']=='Iris-virginica'].mean()
media_Iris_Virginica


# d. Adicione uma única coluna com a média de 'sepal length' para cada um dos tipos de íris indicados na coluna "class". Utilize o loop for e faça isso sem utilizar métodos que não foram ensinados na aula de hoje.

# In[9]:


df['Media_Sepal_length']=0
df


# In[10]:


for idx in df.index:
    #print(df.loc[idx,'Class'])
    if df.loc[idx,'Class']=='Iris-setosa':
        df.loc[idx,'Media_Sepal_length']=media_Iris_Setosa.sepal_length

        
    elif df.loc[idx,'Class']=='Iris-versicolor':
        df.loc[idx,'Media_Sepal_length']=media_Iris_Versicolor.sepal_length

        
    elif df.loc[idx,'Class']=='Iris-virginica':
        df.loc[idx,'Media_Sepal_length']=media_Iris_Virginica.sepal_length


df
    


# In[ ]:





# e. Crie uma coluna de volume sabendo que o volume representa (pi x petallength x sepal_length^2)/3

# In[12]:


df['Volume']=(np.pi*df['petal_length']*df['sepal_length']**2)/3
df


# f. Salve apenas o valor da classe, da média do sepal length e do volume desse dataset em um arquivo csv sem a coluna de index.

# In[20]:


df2=df.loc[:,['Class','Media_Sepal_length','Volume']]


# In[21]:


df2


# In[24]:


df2.to_csv("tabela_processada2.csv", sep=",",index=False)


# In[ ]:




