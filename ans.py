
# coding: utf-8

# In[5]:

import pandas as pd
import datetime
x = pd.read_excel("C:\\Users\\ri20099215\\Desktop\\Assignmenttt\\Sample - Superstore.xls")
df = pd.DataFrame(x)
df


# In[17]:

df.groupby(df['Order Date'].dt.strftime('%B'))['Profit'].sum()


# In[50]:

filter = df['Profit'].max()
df.groupby('Category')["Customer Name"].where(filter,inplace=True)


# In[73]:

x = pd.read_excel("C:\\Users\\ri20099215\\Desktop\\Assignmenttt\\Sample - Superstore.xls")
df2 = pd.DataFrame(x)
df2


# In[98]:

df2.groupby('Category')['Customer Name'].agg({'Profit':'max'})


# In[94]:




# In[100]:

df2.groupby('Ship Date')['Profit'].sum()


# In[107]:

x = df2.groupby(df2['Order Date'].dt.strftime('%B'))["Profit"].min()
x


# In[109]:

x.min()


# In[123]:

filter = df2['Order Date'].dt.strftime('%B') == 'November'
l = df2['Category'].where(filter)
l


# In[ ]:



