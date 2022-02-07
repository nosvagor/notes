#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Math prerequisites
# ### LECTURE: Min/max and argmin/max
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import numpy as np
import torch


# # Using numpy

# In[ ]:


# create a vector
v = np.array([ 1,40,2,-3 ])

# find and report the maximum and minimum values
minval = np.min(v)
maxval = np.max(v)

print('Min,max: %g,%g' %(minval,maxval) )


# now for the argmin/max
minidx = np.argmin(v)
maxidx = np.argmax(v)

print('Min,max indices: %g,%g' %(minidx,maxidx) ), print(' ')

# confirm
print(f'Min val is { v[minidx] }, max val is { v[maxidx] }')


# In[ ]:


# repeat with matrix
M = np.array([ [0,1,10], [20,8,5] ])
print(M), print(' ')

# various minima in this matrix!
minvals1 = np.min(M)        # minimum from ENTIRE matrix
minvals2 = np.min(M,axis=0) # minimum of each column (across rows)
minvals3 = np.min(M,axis=1) # minimum of each row (across columns)

# print them out
print(minvals1)
print(minvals2)
print(minvals3)


# In[ ]:


# various minima in this matrix!
minidx1 = np.argmin(M)        # minimum from ENTIRE matrix
minidx2 = np.argmin(M,axis=0) # minimum of each column (across rows)
minidx3 = np.argmin(M,axis=1) # minimum of each row (across columns)

# print them out
print(M), print(' ') # reminder
print(minidx1)
print(minidx2)
print(minidx3)


# # Now using pytorch

# In[ ]:


# create a vector
v = torch.tensor([ 1,40,2,-3 ])

# find and report the maximum and minimum values
minval = torch.min(v)
maxval = torch.max(v)

print('Min,max: %g,%g' %(minval,maxval) )


# now for the argmin/max
minidx = torch.argmin(v)
maxidx = torch.argmax(v)

print('Min,max indices: %g,%g' %(minidx,maxidx) ), print(' ')

# confirm
print(f'Min val is { v[minidx] }, max val is { v[maxidx] }')


# In[ ]:


# repeat with matrix
M = torch.tensor([ [0,1,10], [20,8,5] ])
print(M), print(' ')

# various minima in this matrix!
min1 = torch.min(M)        # minimum from ENTIRE matrix
min2 = torch.min(M,axis=0) # minimum of each column (across rows)
min3 = torch.min(M,axis=1) # minimum of each row (across columns)

# print them out
print(min1), print(' ')
print(min2), print(' ')
print(min2.values)
print(min2.indices)


# In[ ]:


min2.count

