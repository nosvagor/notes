#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: ANNs
# ### LECTURE: Depth vs. breadth: number of parameters
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import numpy as np
import torch
import torch.nn as nn


# In[ ]:


# build two models

widenet = nn.Sequential(
    nn.Linear(2,4),  # hidden layer
    nn.Linear(4,3),  # output layer
    )


deepnet = nn.Sequential(
    nn.Linear(2,2),  # hidden layer
    nn.Linear(2,2),  # hidden layer
    nn.Linear(2,3),  # output layer
    )

# print them out to have a look
print(widenet)
print(' ')
print(deepnet)


# In[ ]:


widenet.


# # Peeking inside the network

# In[ ]:


# check out the parameters
for p in deepnet.named_parameters():
  print(p)
  print(' ')


# In[ ]:


# count the number of nodes ( = the number of biases)

# named_parameters() is an iterable that returns the tuple (name,numbers)
numNodesInWide = 0
for p in widenet.named_parameters():
  if 'bias' in p[0]:
    numNodesInWide += len(p[1])

numNodesInDeep = 0
for paramName,paramVect in deepnet.named_parameters():
  if 'bias' in paramName:
    numNodesInDeep += len(paramVect)


print('There are %s nodes in the wide network.' %numNodesInWide)
print('There are %s nodes in the deep network.' %numNodesInDeep)


# In[ ]:


# just the parameters
for p in widenet.parameters():
  print(p)
  print(' ')


# In[ ]:


# now count the total number of trainable parameters
nparams = 0
for p in widenet.parameters():
  if p.requires_grad:
    print('This piece has %s parameters' %p.numel())
    nparams += p.numel()

print('\n\nTotal of %s parameters'%nparams)


# In[ ]:


# btw, can also use list comprehension

nparams = np.sum([ p.numel() for p in widenet.parameters() if p.requires_grad ])
print('Widenet has %s parameters'%nparams)

nparams = np.sum([ p.numel() for p in deepnet.parameters() if p.requires_grad ])
print('Deepnet has %s parameters'%nparams)


# In[ ]:





# In[ ]:


# A nice simple way to print out the model info.
from torchsummary import summary
summary(widenet,(1,2))


### NOTE ABOUT THE CODE IN THIS CELL:
# torchsummary is being replaced by torchinfo.
# If you are importing these libraries on your own (via pip), then see the following website:
#        https://pypi.org/project/torch-summary/
# However, torchsummary will continue to be supported, so if the code in this cell works (meaning torchsummary is already installed), 
# then you don't need to do anything!


# In[ ]:




