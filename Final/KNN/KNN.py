#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd


# In[15]:


dt.isnull().any()
fillup="No"
dt.Accident=dt.Accident.fillna(fillup)
dt


# In[16]:


from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


# In[17]:


Speed=(80,80,30,25,40,20,50,120,35,260,90)
Road_Quality=["Bad","Bad","Good","Good","Bad","Bad","Bad","Bad","Bad","Good","Good"]
Accident=["Yes","Yes","No","No","No","No","No","Yes","No","Yes","No"]
encode = preprocessing.LabelEncoder()
Encoded_Accident = encode.fit_transform(Accident)
Encoded_Road_Quality = encode.fit_transform(Road_Quality)
print(Encoded_Accident)
print(Encoded_Road_Quality)


# In[18]:



f = list(zip(Speed,Encoded_Road_Quality))
f


# In[19]:


model = KNeighborsClassifier(n_neighbors=6)
model.fit(f,Encoded_Accident)


# In[20]:


prediction = model.predict([[100,0]])
print("KNN prediction: \n 0 for Yes and 1 for No")
print(prediction)


# In[21]:



print("Accuracy= ")
acc=(model.score(f,Encoded_Accident))*100
print(acc)

