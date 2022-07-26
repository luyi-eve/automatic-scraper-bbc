#!/usr/bin/env python
# coding: utf-8

# # Automate Scraper!!
# 
# * We're going to write a scraper!!!
# * Website: https://www.bbc.com

# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get("https://www.bbc.com")
doc = BeautifulSoup(response.text)


# In[8]:


# Grab all of the titles
titles = doc.select(".media__title a")
titles


# In[13]:


rows = []

for title in titles:
    row = {}
    
    # title
    row["title"] = title.text.strip()
    # link
    row["link"] = title["href"]
    
    # then add it to our list of rows
    rows.append(row)

df = pd.DataFrame(rows)
df


# In[14]:


#df.to_csv("bbc.csv",index=False)


# In[ ]:




