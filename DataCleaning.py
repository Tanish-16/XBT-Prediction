#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing the required libraries


# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[ ]:


#Reading the csv file


# In[ ]:


data=pd.read_csv(r'C:\Users\Admins\Desktop\bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv')


# In[ ]:


#Checking the dimensions and the first and last few entries of the dataset 


# In[ ]:


data.shape
data.head()
data.tail()


# In[ ]:


#Number of null entries in the dataset 


# In[ ]:


data.isnull().sum()


# In[ ]:


#Dropping the row having either Timestamp, Open, High, Low, Close, Volume_(BTC), Volume_(Currency) entry as null.


# In[ ]:


data=data.dropna(subset=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume_(BTC)', 'Volume_(Currency)'], how='any')


# In[ ]:


data.shape
data.isnull().sum()


# In[ ]:


#Reset the indexes


# In[ ]:


data = data.reset_index()
data.head()
del data['index']

#Applying feature scaling.
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
data[['Open', 'High', 'Low', 'Close', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price']]=sc.fit_transform(data[['Open', 'High', 'Low', 'Close', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price']])

data.tail()
