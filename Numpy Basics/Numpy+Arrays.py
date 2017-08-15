
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

arr=np.array([1,2,3])


# In[3]:

arr


# In[4]:

len(arr)


# In[5]:

arr[2]


# In[6]:

type(arr[2])


# In[7]:

arr.dtype


# In[8]:

arr32=np.array([1,2,3],dtype=np.int32)


# In[9]:

arr32


# In[10]:

arr64=np.array([1,2,3],dtype=np.int64)
arr64


# In[11]:

arr*arr


# In[12]:

v1=np.random.rand(1000000)
v2=np.random.rand(1000000)


# In[13]:

v1


# In[14]:

v2


# In[15]:

v1*v2


# In[16]:

get_ipython().magic('time v1*v2')


# In[17]:

#to get the dot prod
np.dot(arr,arr)


# In[18]:

arr@arr


# In[19]:

mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat


# In[20]:

v=np.arange(12)


# In[21]:

v


# In[22]:

#v.reshape((4,3))
v.reshape(4,3)


# In[23]:

mat=np.arange(12).reshape((4,3))
mat


# In[24]:

mat.shape


# In[25]:

mat2=mat.reshape((3,4))
mat2


# In[26]:

#changing a value at second row and third column----notice how both mat and mat2 get changed
mat[1,2]=17


# In[27]:

mat


# In[28]:

mat2


# In[29]:

#to transpose a matrix
mat.T


# In[30]:

mat


# In[ ]:



