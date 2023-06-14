#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')
parent_theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')
df.head()


# In[2]:


parent_theme.head()


# In[3]:


theme.head(50)


# In[4]:


parent_theme.head(50)


# In[8]:


merged = df.merge(parent_theme, left_on='parent_theme', right_on='name')
merged.drop(columns='name_y', inplace=True)
merged.head()


# In[12]:


merged_df = merge[merged['is_licensed']]
licensed.head()

star_wars = licensed[licensed['parent_theme']=='Star Wars']

the_force = (star_wars.shape[0]/licensed.shape[0])

print(the_force)


# In[ ]:




