#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Importing the libraries

import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor


# In[8]:


# loading the datasets 
movies_data=pd.read_csv('C:/Users/LENOVO/Downloads/movies.dat', sep='::',engine='python',encoding='latin-1',names=['Movieid','Title','Genres'])
movies_data.head()


# In[9]:


movies_data.shape


# In[10]:


users_data=pd.read_csv('C:/Users/LENOVO/Downloads/users.dat', sep='::', engine='python', encoding='latin-1',names=['Userid','Gender','Age','Occupation','Zipcode'])
users_data.head()


# In[11]:


users_data.shape


# In[12]:


ratings_data=pd.read_csv('C:/Users/LENOVO/Downloads/ratings.dat', sep='::',engine='python',encoding='latin-1',names=['Userid','Movieid','Ratings','Timestamp'])
ratings_data.head()


# In[13]:


ratings_data.shape


# In[14]:


# merging movie data with respect to ratings data

ratings_data=movies_data.merge(ratings_data,on='Movieid',how='inner')
ratings_data.head()


# In[15]:


# merging the ratings data with respect to users data and creating new data set

main_data=ratings_data.merge(users_data,on='Userid',how='inner')
main_data.head()


# In[16]:


main_data.shape


# In[17]:


main_data.isnull().sum() # checking for null values


# In[18]:


main_data.info() # checking the information about the dataset


# In[20]:


# user ratings for a movies 

movie_rating=main_data[main_data['Title'].str.contains('Toy Story')]
movie_rating


# In[30]:


# visual representation

movie_rating.groupby(['Title','Ratings']).size().unstack().plot(kind='bar',stacked=False, legend=True)
plt.figure(figsize=(15,8))
plt.show()


# In[32]:


movie_rating.groupby(['Age','Ratings']).size().unstack().plot(kind='bar',stacked=False, legend=True)
plt.figure(figsize=(20,8))
plt.show()

