#!/usr/bin/env python
# coding: utf-8

# # Project made by Salma Moukrim / projet fait par Salma Moukrim
# we will see the sales amount in USD for each month.
# 1- Data collection from a CSV file, we merge 12 csv file into one csv file.
# each cvs file is about data in one month.
# 2- data cleaning and eliminate missing values
# 3-data visualisation

# In[2]:


# importer les packages 
import os 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[14]:


files=[file for file in os.listdir(r'C:\Users\HP\Downloads\sales_assesment')]
for file in files:
    print(file)
    


# In[15]:


# regrouper ces fichiers dans un seul fichier 
path=r'C:\Users\HP\Downloads\sales_assesment'
all_data=pd.DataFrame()
# j'ai créer une dataframe et la remplir
for file in files:
    current_data=pd.read_csv(path +'/'+ file)
    all_data=pd.concat([all_data,current_data])
print(all_data)    


# In[16]:


#le code qui est juste et qui marche
path = r'C:\Users\HP\Downloads\sales_assesment'
all_data = pd.DataFrame()  # Créez un DataFrame vide pour stocker les données combinées

# Parcourez tous les fichiers dans le répertoire
for file in os.listdir(path):
    if file.endswith('.csv'):  # Assurez-vous que le fichier est un fichier CSV
        current_data = pd.read_csv(os.path.join(path, file))
        all_data = pd.concat([all_data, current_data], ignore_index=True)
print(all_data)        
        


# In[17]:


#convertir la data frame all_data en fichier csv
all_data.to_csv(os.path.join(path,'all_data.csv'))


# In[18]:


all_data.dtypes


# In[19]:


all_data.isnull().sum()


# In[20]:


#supprimer les valeurs manquantes 
all_data=all_data.dropna(how='all')
all_data.shape


# # what is the month where we achieved the most turnover?
# 

# In[21]:


all_data


# In[22]:


def month(x):
    return x.split('/')[0]
month('12/30/19 00:01')


# In[23]:


all_data['Month']=all_data['Order Date'].apply(month)
all_data


# In[20]:


all_data['Month'].unique()


# In[21]:


all_data=all_data[all_data['Month']!='Order Date']
all_data['Month'].unique()


# In[22]:


all_data.dtypes


# In[27]:


all_data['Month']=all_data['Month'].astype(int)
all_data.dtypes


# In[28]:


all_data['Price Each']=all_data['Price Each'].astype(float)
all_data['Quantity Ordered']=all_data['Quantity Ordered'].astype(int)
all_data.dtypes


# In[30]:


all_data['Sales']=all_data['Quantity Ordered']*all_data['Price Each']
all_data


# In[33]:


all_data.groupby('Month')['Sales'].sum()


# In[34]:


months=range(1,13)
plt.bar(months,all_data.groupby('Month')['Sales'].sum())
plt.xticks(months)
plt.ylabel('Sales in USD')
plt.xlabel('Month number')
plt.show()


# In[4]:


all_data.dtypes


# In[5]:


#convertir le fichier csv en dataframe
all_data = pd.DataFrame()


# In[6]:


# convertir le fichier csv into a dataframe
all_data=pd.read_csv('all_data.csv')


# In[7]:


all_data


# In[8]:


def month(x):
    return x.split('/')[0]
month('12/30/19 00:01')


# In[9]:


all_data['Month']=all_data['Order Date'].apply(month)
all_data


# In[10]:


def month(x):
    return x.split('/')[0]


# In[11]:


all_data['Month']=all_data['Order Date'].apply(month)
all_data


# In[12]:


all_data['Order Date'].dtypes


# In[13]:


all_data['Order Date'] = all_data['Order Date'].astype(str)


# In[14]:


all_data['Month'] = all_data['Order Date'].apply(month)


# In[15]:


all_data


# In[16]:


#supprimer les valeurs manquantes 
all_data=all_data.dropna(how='all')
all_data.shape


# In[17]:


all_data


# In[18]:


all_data.dropna(inplace=True)


# In[19]:


all_data


# In[ ]:




