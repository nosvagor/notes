#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Data matrices and loaders
# ### LECTURE: Anatomy of a torch dataset and dataloader
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import numpy as np
import torch
from torch.utils.data import DataLoader,TensorDataset


# # Datasets

# In[ ]:


# create some data in numpy

nObservations = 100
nFeatures = 20

data = np.random.randn(nObservations,nFeatures)


# In[ ]:


# Convert to pytorch tensor
dataT = torch.tensor( data ) 

# print out some information
print('Numpy data:')
print(type(data))
print(data.shape) # numpy -> .shape
print(data.dtype)
print(' ')

print('Tensor data:')
print(type(dataT))
print(dataT.size()) # torch -> .size()
print(dataT.dtype)
print(' ')


# In[ ]:


# Sometimes you need to convert data types

dataT2 = torch.tensor( data ).float()
print(dataT2.dtype)

# "long" is for ints
dataT3 = torch.tensor( data ).long()
print(dataT3.dtype)


# In[ ]:


# Convert tensor into PyTorch Datasets

# dataset = TensorDataset(data) # not a tensor!
dataset = TensorDataset(dataT)

# dataset is a two-element tuple comprising data,labels
dataset.tensors[0]


# In[ ]:


# Let's try again with labels
labels = torch.ceil(torch.linspace(.01,4,nObservations))

# transform to an actual matrix (column vector)
labels = labels.reshape(( len(labels),1 ))
# print( labels )

# now make another dataset
dataset = TensorDataset(dataT,labels)
print( dataset.tensors[0].size() )
print( dataset.tensors[1].size() )

# for comparison
print( np.shape(np.random.randint(5,size=nObservations)) )


# # DataLoaders

# In[ ]:


# create a dataloader object
batchsize = 25
dataloader = DataLoader(dataset,batch_size=batchsize)#,shuffle=True,drop_last=True)

dataloader.dataset.tensors[0].size()


# In[ ]:


# sizes of each batch
for dat,labs in dataloader:
  print('BATCH INFO:')
  print(dat.size())
  print(labs.size())
  print(' ')


# In[ ]:


# inspect the labels
for dat,labs in dataloader:
  print(labs.T)
  print(' ')


# In[ ]:


# try again with shuffling (shuffling happens during iterations)
# dataloader = DataLoader(dataset,batch_size=batchsize,shuffle=True)

for dat,labs in dataloader:
  print(labs.T)
  print(' ')


# In[ ]:


# To get only one batch (e.g., for testing)

dat,labs = next(iter(dataloader))

labs

