#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf


# In[2]:


import pandas as pd
import configparser
import sqlite3


# In[3]:


config = configparser.ConfigParser()
config.read(r"C:\Users\Renuka\OneDrive\Desktop\config1.ini")
companies = dict(config.items('Companies'))
print(companies)


# In[4]:


conn = sqlite3.connect('finance.db')
cursor = conn.cursor()


# In[5]:


for ticker in companies.values():
    data = yf.download(ticker)
    print(data)


# In[6]:


# Add company name column
data['company_name'] = ticker


# In[7]:


# Load data into database
data.to_sql('yahoo_finance_data13', conn, if_exists='append', index=False)


# In[8]:


# Close database connection
conn.close()


# In[ ]:




