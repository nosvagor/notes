#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Math prerequisites
# ### LECTURE: Mean and variance
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import numpy as np


# In[ ]:


# create a list of numbers to compute the mean and variance of
x = [1,2,4,6,5,4,0]
n = len(x)

# compute the mean
mean1 = np.mean(x)
mean2 = np.sum(x) / n

# print them
print(mean1)
print(mean2)


# In[ ]:


# variance

var1 = np.var(x)
var2 = (1/(n-1)) * np.sum( (x-mean1)**2 )

print(var1)
print(var2)


# In[ ]:


# uh oh!

var3 = np.var(x,ddof=1)

print(var3)
print(var2)


# In[ ]:


# does it matter for large N? 

N = 10000
x = np.random.randint(0,high=20,size=N)

var0 = np.var(x,ddof=0) # default
var1 = np.var(x,ddof=1) # unbiased

print(var0)
print(var1)

