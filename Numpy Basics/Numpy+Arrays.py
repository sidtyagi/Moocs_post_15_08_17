
# coding: utf-8

# In[6]:

import numpy as np


# In[7]:

arr=np.array([1,2,3])


# In[8]:

arr


# In[9]:

len(arr)


# In[10]:

arr[2]


# In[11]:

type(arr[2])


# In[12]:

arr.dtype


# In[13]:

arr32=np.array([1,2,3],dtype=np.int32)


# In[14]:

arr32


# In[15]:

arr64=np.array([1,2,3],dtype=np.int64)
arr64


# In[16]:

arr*arr


# In[17]:

v1=np.random.rand(1000000)
v2=np.random.rand(1000000)


# In[18]:

v1


# In[19]:

v2


# In[20]:

v1*v2


# In[21]:

get_ipython().magic('time v1*v2')


# In[22]:

#to get the dot prod
np.dot(arr,arr)


# In[23]:

arr@arr


# In[24]:

mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat


# In[25]:

v=np.arange(12)


# In[26]:

v


# In[27]:

#v.reshape((4,3))
v.reshape(4,3)


# In[28]:

mat=np.arange(12).reshape((4,3))
mat


# In[29]:

mat.shape


# In[30]:

mat2=mat.reshape((3,4))
mat2


# In[31]:

#changing a value at second row and third column----notice how both mat and mat2 get changed
mat[1,2]=17


# In[32]:

mat


# In[33]:

mat2


# In[34]:

#to transpose a matrix
mat.T


# In[35]:

mat


# In[36]:

#Slicing
nums=[1,2,3,4,5]
nums[2:5]


# In[37]:

v=np.arange(1,6)
v[2:4]


# In[38]:

arr=np.arange(12).reshape(3,4)
arr


# In[39]:

#to get a particular row
arr[0]


# In[40]:

#to get second row, second column
arr[1][1]


# In[41]:

#to pick every row, and then the second element of every row
arr[:,1]


# In[42]:

arr[:,1].reshape(3,1)


# In[43]:

#slicing can be used on both axes
arr[1:,2:]


# In[44]:

#can be used to set values as well--this is broadcasting --setting the scalar
arr[1:,2:]=7


# In[45]:

arr


# In[46]:

#boolean indexing
#in order to select parts of an array that satisfy some threshold
arr=np.arange(3)
arr[np.array([True,False,True])]


# In[47]:

arr>=1


# In[48]:

arr


# In[49]:

arr=np.arange(10)


# In[50]:

arr


# In[51]:

arr[(arr>2)&(arr<7)]


# In[52]:

arr[(arr>7)|(arr<2)]


# In[53]:

arr[~(arr>7)]


# In[54]:

#understanding broadcasting


# In[58]:

arr=np.arange(3)
print(arr)


# In[60]:

arr+4
#scalar to vector--adds the scalar to every element of array


# In[61]:

arr / 7


# In[62]:

arr**2


# In[63]:

#let's create a matrix of 3 by 3
mat=np.arange(9).reshape([3,3])


# In[64]:

mat


# In[66]:

#let's create a vector of 3
vec=np.arange(3)
vec


# In[67]:

mat+vec


# In[73]:

v1=np.arange(3)
v2=np.arange(3).reshape((3,1))


# In[69]:

v2


# In[82]:

#dir(v2)


# In[75]:

v2.shape


# In[76]:

v1


# In[83]:

v2


# In[80]:

v1.shape,v2.shape


# In[85]:

v1+v2
#v1 will be extended down and v2 will be extended to a row of zeroes,to a row of 1's and to a row of 2's
#see the video snippet at 2:30 of 'Understanding broadcasting'


# In[84]:

#np always tries to find out the best match
np.arange(3)+np.arange(4)


# In[86]:

#understanding array operations
v=np.arange(12).reshape(4,3)
v


# In[87]:

#to view the attributes and methods of v; note that attributes that start with 2 underscore have a special meaning, they are
#called dunder methods, meaning double underscore
dir(v)


# In[88]:

#when i type v dot and hit enter, jupyter won't show me the dunder methods


# In[89]:

#to do the transpose,use
v.T


# In[91]:

#even if  one element is true
v.any()


# In[92]:

#return true if all element are true
v.all()


# In[93]:

if v:
    print("v is true")


# In[94]:

#to get the zen of python
import this


# In[95]:

#since first element is 0, we get the prod as 0
v.prod()


# In[96]:

#to work row-wise, sums 
v.sum(axis=1)


# In[97]:

v


# In[99]:

#to get the sum of each column
v.sum(axis=0)


# In[100]:

#to mutate the array, w/o affecting the original one
v1=v.copy()


# In[101]:

v1[0,0]=1000


# In[102]:

v1


# In[103]:

v


# In[107]:

#methods for serialization, send an array over a socket to be written to a file or DB for later retrieval
#we use python's pickle protocol
data=v.dumps()
data


# In[108]:

type(data)
#observe that is a stream of bytes


# In[109]:

v2=np.loads(data)


# In[110]:

v2


# In[111]:

#instead of v.prod , we can also call the prod on the np module
np.prod(v)


# In[112]:

#understanding ufuncs--universal functions
np.sin(np.pi/2)
#note that sin expects inout in radians


# In[113]:

#why numpy bothers to define a function that is already defined in python
v=np.arange(-3,3)
#now we can call numpy.sin on the vector itself
np.sin(v)


# In[114]:

#ufuncs are universal functions --mening they can work on both scalars(plane numbers) and arrays
#take an example-
def noneg(num):
    if num<0:
        return 0
    return num


# In[115]:

noneg(-13)


# In[116]:

noneg(13)


# In[117]:

v


# In[118]:

noneg(v)


# In[119]:

#to avoid this we use decorators
#decorators are functions that use functions as arguments and return functions
#whenever you see me writing @np.vectorize, and then the definition of noneg===>this is very much like writing the definition
# noneg and then saying that noneg is equal to np.vectorize of noneg


# In[120]:

@np.vectorize
def noneg(num):
    if num<0:
        return 0
    return num


# In[121]:

noneg(v)


# In[122]:

#the above s equal to below
def noneg(num):
    if num<0:
        return 0
    return num
noneg=np.vectorize(noneg)


# In[123]:

noneg(v)


# In[124]:

noneg(3)


# In[125]:

noneg(3).shape


# In[126]:

#so the function now works on both scalar and vector


# In[127]:

np.nan


# In[ ]:

#Pandas
#numpy is great for working with matrices of the same type(integers,floats etc.
#but data in the real world is often composed of mixed types--heterogenous data
#pandas support mixed types with ease

