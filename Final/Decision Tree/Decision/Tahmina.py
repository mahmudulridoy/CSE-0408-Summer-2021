#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from sklearn import tree


# In[9]:


df = pd.read_csv("E:\GIT\-CSE-0408-Summer-2021\Final\Decision\Tahmina.csv")


# In[10]:


x = df.iloc[:,:-1]


# In[11]:


x


# In[12]:


y=df.iloc[:,3]


# In[13]:


y


# In[14]:


classify_ = tree.DecisionTreeClassifier()


# In[15]:


classify_ =classify_.fit(x,y)


# In[16]:


prediction_ = classify_.predict([[190,70,43]])


# In[17]:


prediction_


# In[ ]:




