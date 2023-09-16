#!/usr/bin/env python
# coding: utf-8

# In[12]:


#importing libraries 

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[13]:


# Loading the dataset 

Df=pd.read_csv('C:/Users/LENOVO/Downloads/advertising.csv')
Df.head()


# In[14]:


Df.shape


# In[15]:


Df.info()


# In[16]:


Df.isnull().sum()


# In[17]:


Df.describe()


# In[18]:


Df.columns


# In[20]:


X=Df.drop(columns=['TV','Sales'],axis=1)
Y=Df['Sales']


# In[21]:


print(X)


# In[23]:


print(Y)


# In[24]:


# Spliting the training data and test data

X_train, X_test, Y_train, Y_test =train_test_split(X,Y, test_size=0.2, random_state=2)


# In[26]:


print(X.shape,X_train.shape,X_test.shape)


# In[27]:


# model Training 

model=LinearRegression()


# In[28]:


model.fit(X_train,Y_train)


# In[29]:


print('intercept:=b0', model.intercept_)
print('slope:=b1 & b2', model.coef_)


# In[30]:


X_train_prediction=model.predict(X_train)


# In[31]:


print(X_train_prediction)


# In[32]:


r2=model.score(X_train, Y_train)


# In[33]:


print(r2)


# In[34]:


Prediction_model=[[100,100,100]]


# In[37]:


print('Sales of TV, Radio and Newspaper is :', Prediction_model)

