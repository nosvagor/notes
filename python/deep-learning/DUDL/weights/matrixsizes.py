#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Weight inits and investigations
# ### LECTURE: Explanation of weight matrix sizes
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import torch
import torch.nn as nn


# # Create a model and inspect its weight matrices sizes

# In[ ]:


# build a model
aModel = nn.Sequential(
    nn.Linear(10,14),  # input layer
    nn.Linear(14,19),  # hidden layer
    nn.Linear(19,8),   # output layer
      )

aModel


# In[ ]:


# print the sizes of the weights matrices in each layer
for i in range(len(aModel)):
  print( aModel[i].weight.shape )


# # Build a model with inconsistent layer shapes

# In[ ]:


M2 = nn.Sequential(
    nn.Linear(10,14),  # input layer
    nn.Linear(14,9),   # hidden layer
    nn.Linear(19,8),   # output layer
      )

for i in range(len(M2)):
  print( M2[i].weight.shape )


# # Test both models with fake data

# In[ ]:


# generate the data
nsamples = 5
nfeatures = 10

fakedata = torch.randn(nsamples,nfeatures)


# In[ ]:


# test the first model

# does the size of the output make sense?
aModel(fakedata).shape


# In[ ]:


# test the second model

# does the size of the output make sense?
M2(fakedata).shape


# In[ ]:




