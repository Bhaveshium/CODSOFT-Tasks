#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the required libraries 

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# In[3]:


# Loading the dataset

df=pd.read_csv('C:/Users/LENOVO/Downloads/Iris.csv')
df.head()


# In[4]:


# Getting information about data 

df.info()


# In[5]:


# checking null values

df.isnull().sum() 


# In[6]:


# Getting statstical data 
df.describe()


# In[7]:


# to display number of samples on each class

df['species'].value_counts()


# In[8]:


# Visual representation

df['sepal_length'].hist()


# In[9]:


df['sepal_width'].hist()


# In[10]:


df['petal_length'].hist()


# In[11]:


df['petal_width'].hist()


# In[12]:


# Scatter plot 
colors=['red','orange','blue']
species=['Iris-setosa','Iris-versicolor','Iris-virginica']

for i in range(3):
    x=df[df['species']==species[i]]
    plt.scatter(x['sepal_length'],x['sepal_width'],c=colors[i],label=species[i])
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.legend()


# In[13]:


colors=['red','orange','blue']
species=['Iris-setosa','Iris-versicolor','Iris-virginica']

for i in range(3):
    x=df[df['species']==species[i]]
    plt.scatter(x['petal_length'],x['petal_width'],c=colors[i],label=species[i])
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.legend()


# In[14]:


# coorelation matrix
df.corr()


# In[15]:


Corr=df.corr()
fig, ax=plt.subplots(figsize=(5,4))
sns.heatmap(Corr, annot=True, ax=ax)


# In[16]:


# Label Encoder

le=LabelEncoder()


# In[17]:


df['species']=le.fit_transform(df['species'])
df.head()


# In[18]:


# Model training 

X=df.drop(columns=['species'])
Y=df['species']


# In[20]:


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=2)


# In[21]:


print(X.shape,X_train.shape,X_test.shape)


# In[22]:


model=KNeighborsClassifier()


# In[23]:


model.fit(X_train, Y_train)


# In[24]:


# accuracy on training data 

X_train_prediction=model.predict(X_train)


# In[25]:


print(X_train_prediction)


# In[26]:


training_data_accuracy =accuracy_score(Y_train, X_train_prediction)

print('Accuracy score of training data :', training_data_accuracy )


# In[27]:


# Accuracy on test data 

X_test_prediction =model.predict(X_test)


# In[28]:


print(X_test_prediction)


# In[29]:


testing_data_accuracy=accuracy_score(Y_test,X_test_prediction)

print('Accuracy score of testing data :', testing_data_accuracy)

