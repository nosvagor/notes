#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Math prerequisites
# ### LECTURE: Matrix multiplication
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import numpy as np
import torch


# # Using numpy

# In[ ]:


# create some random matrices
A = np.random.randn(3,4)
B = np.random.randn(4,5)
C = np.random.randn(3,7)

# try some multiplications...
print(np.round( A@B   ,2)), print(' ')
# print(np.round( A@C   ,2)), print(' ')
# print(np.round( B@C   ,2)), print(' ')
print(np.round( C.T@A ,2))


# # Using pytorch

# In[ ]:


# create some random matrices
A  = torch.randn(3,4)
B  = torch.randn(4,5)
C1 = np.random.randn(4,7)
C2 = torch.tensor( C1,dtype=torch.float )

# try some multiplications...
# print(np.round( A@B   ,2)), print(' ')
# print(np.round( A@B.T ,2)), print(' ')
print(np.round( A@C1  ,2)), print(' ')
print(np.round( A@C2  ,2))

