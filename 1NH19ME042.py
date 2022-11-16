#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


df=pd.read_csv("C:/Users/Admin/Desktop/weight-heightt.csv")


# In[7]:


df


# In[8]:


df.info()


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df.head(-10)


# In[13]:


df.keys()


# In[15]:


df.values


# In[16]:


df.head(5)


# In[20]:


df.isnull().sum()
            
    
             


# In[22]:


df.shape


# # outlier detection using standard deviation

# In[24]:


plt.hist(df.Height,bins=20,width=0.8)
plt.xlabel("height")
plt.ylabel("count")
plt.show()


# In[26]:


df.Height.min()


# In[37]:


a=df.Height.mean()
a


# In[30]:


x=df.Height.std()
x   


# In[40]:


b=cut_off=x*3
b


# In[38]:





# In[41]:


lower,upper=a-b,a+b


# In[42]:


lower,upper


# In[44]:


df[(df.Height>upper)|(df.Height<lower)]


# In[47]:


df_no_outlier_std_dev=df[(df.Height<upper)&(df.Height>lower)]
df_no_outlier_std_dev.head(10)


# In[49]:


df_no_outlier_std_dev.shape


# #outlier detection using zscore

# In[53]:


df['zscore'] = (df.Height-df.Height.mean())/df.Height.std()


# In[54]:


df.head()


# In[57]:


df[df['zscore']>3]


# In[58]:


df[df['zscore']<-3]


# In[64]:


df[(df.zscore<-3)|(df.zscore>3)]


# In[66]:


df_no_otliers=df[(df.zscore>-3)&(df.zscore<3)]
df_no_otliers.head()


# In[67]:


df_no_otliers


# # outliers with interquartile range

# In[75]:


import seaborn as sns
import numpy as np


# In[76]:


data=[6,1,2,3,4,5,50]
sort_data=np.sort(data)
sort_data


# In[81]:


Q1=np.percentile(data,25)
Q2=np.percentile(data,50)
Q3=np.percentile(data,75)
print('Q1 25 percentile of the given data is',Q1)
print('Q2 50 percentile of the given data is',Q2)
print('Q3 75 percentile of the given data is',Q3)
IQR=Q3-Q1
print('interquartile range is',IQR)


# In[83]:


low_lim=Q1-1.5*IQR
up_lim=Q3+1.5*IQR
print('low_lim is ',low_lim)
print('up_lim is',up_lim)


# In[84]:


sns.boxplot(data)


# In[ ]:




