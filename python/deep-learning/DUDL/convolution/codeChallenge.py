#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Convolution and transformations
# ### LECTURE: CodeChallenge: choose the parameters
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[1]:


# import libraries
import numpy as np
import torch
import torch.nn as nn


# # Sample problem

# ### Convolve an image of size 1x256x256 to produce a 1x252x84 result

# In[2]:


# parameters
inChans  = 1 # RGB
imsize   = [256,256]
outChans = 1
krnSize  = 7 # should be an odd number
stride   = (1,3)
padding  = 1

# create the instance
c = nn.Conv2d(inChans,outChans,krnSize,stride,padding)

# create an image
img = torch.rand(1,inChans,imsize[0],imsize[1])

# run convolution and compute its shape
resimg = c(img)
empSize = torch.squeeze(resimg).shape

# compute the size of the result according to the formula
expectSize = np.array([outChans,0,0],dtype=int)
expectSize[1] = np.floor( (imsize[0]+2*padding-krnSize)/stride[0] ) + 1
expectSize[2] = np.floor( (imsize[1]+2*padding-krnSize)/stride[1] ) + 1

# check the size of the output
print(f'Expected size: {expectSize}')
print(f'Empirical size: {list(empSize)}')


# # Real problems

# ### 1) Convolve an image of size 3x64x64 to produce a 10x28x28 result

# In[ ]:


# parameters
inChans  = 
imsize   = 
outChans = 
krnSize  = 
stride   = 
padding  = 

# create the instance
c = nn.Conv2d(inChans,outChans,krnSize,stride,padding)

# create an image
img = torch.rand(1,inChans,imsize[0],imsize[1])

# run convolution and compute its shape
resimg = c(img)
empSize = torch.squeeze(resimg).shape

# compute the size of the result according to the formula
expectSize = np.array([outChans,0,0],dtype=int)
expectSize[1] = np.floor( (imsize[0]+2*padding-krnSize)/stride[0] ) + 1
expectSize[2] = np.floor( (imsize[1]+2*padding-krnSize)/stride[1] ) + 1

# check the size of the output
print(f'Expected size: {expectSize}')
print(f'Empirical size: {list(empSize)}')


# ### 2) Convolve an image of size 3x196x96 to produce a 5x66x49 result

# In[ ]:


# parameters
inChans  = 
imsize   = 
outChans = 
krnSize  = 
stride   = 
padding  = 

# create the instance
c = nn.Conv2d(inChans,outChans,krnSize,stride,padding)

# create an image
img = torch.rand(1,inChans,imsize[0],imsize[1])

# run convolution and compute its shape
resimg = c(img)
empSize = torch.squeeze(resimg).shape

# compute the size of the result according to the formula
expectSize = np.array([outChans,0,0],dtype=int)
expectSize[1] = np.floor( (imsize[0]+2*padding-krnSize)/stride[0] ) + 1
expectSize[2] = np.floor( (imsize[1]+2*padding-krnSize)/stride[1] ) + 1

# check the size of the output
print(f'Expected size: {expectSize}')
print(f'Empirical size: {list(empSize)}')


# ### 3) Convolve an image of size 1x32x32 to produce a 6x28x28 result

# In[ ]:


# note: these dimensions are the input -> first hidden layer of the famous LeNet-5

# parameters
inChans  = 
imsize   = 
outChans = 
krnSize  = 
stride   = 
padding  = 

# create the instance
c = nn.Conv2d(inChans,outChans,krnSize,stride,padding)

# create an image
img = torch.rand(1,inChans,imsize[0],imsize[1])

# run convolution and compute its shape
resimg = c(img)
empSize = torch.squeeze(resimg).shape

# compute the size of the result according to the formula
expectSize = np.array([outChans,0,0],dtype=int)
expectSize[1] = np.floor( (imsize[0]+2*padding-krnSize)/stride[0] ) + 1
expectSize[2] = np.floor( (imsize[1]+2*padding-krnSize)/stride[1] ) + 1

# check the size of the output
print(f'Expected size: {expectSize}')
print(f'Empirical size: {list(empSize)}')


# ### 4) Convolve an image of size 3x227x227 to produce a 96x55x55 result

# In[ ]:


# note: these dimensions are the input -> first hidden layer of the famous AlexNet

# parameters
inChans  = 
imsize   = 
outChans = 
krnSize  = 
stride   = 
padding  = 

# create the instance
c = nn.Conv2d(inChans,outChans,krnSize,stride,padding)

# create an image
img = torch.rand(1,inChans,imsize[0],imsize[1])

# run convolution and compute its shape
resimg = c(img)
empSize = torch.squeeze(resimg).shape

# compute the size of the result according to the formula
expectSize = np.array([outChans,0,0],dtype=int)
expectSize[1] = np.floor( (imsize[0]+2*padding-krnSize)/stride[0] ) + 1
expectSize[2] = np.floor( (imsize[1]+2*padding-krnSize)/stride[1] ) + 1

# check the size of the output
print(f'Expected size: {expectSize}')
print(f'Empirical size: {list(empSize)}')


# ### 5) Convolve an image of size 3x224x224 to produce a 64x224x224 result

# In[ ]:


# note: these dimensions are the input -> first hidden layer of the famous VGG-16

# parameters
inChans  = 
imsize   = 
outChans = 
krnSize  = 
stride   = 
padding  = 

# create the instance
c = nn.Conv2d(inChans,outChans,krnSize,stride,padding)

# create an image
img = torch.rand(1,inChans,imsize[0],imsize[1])

# run convolution and compute its shape
resimg = c(img)
empSize = torch.squeeze(resimg).shape

# compute the size of the result according to the formula
expectSize = np.array([outChans,0,0],dtype=int)
expectSize[1] = np.floor( (imsize[0]+2*padding-krnSize)/stride[0] ) + 1
expectSize[2] = np.floor( (imsize[1]+2*padding-krnSize)/stride[1] ) + 1

# check the size of the output
print(f'Expected size: {expectSize}')
print(f'Empirical size: {list(empSize)}')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Answers (don't cheat!)

# In[ ]:


# 1)
inChans  = 3
imsize   = [64,64]
outChans = 10
krnSize  = 9
stride   = (2,2)
padding  = 0

# 2)
inChans  = 3
imsize   = [196,96]
outChans = 5
krnSize  = 5
stride   = (3,2)
padding  = 3

# 3)
inChans  = 1
imsize   = [32,32]
outChans = 6
krnSize  = 5
stride   = (1,1)
padding  = 0

# 4)
inChans  = 3
imsize   = [227,227]
outChans = 96
krnSize  = 11
stride   = (4,4)
padding  = 1

# 5)
inChans  = 3
imsize   = [224,224]
outChans = 64
krnSize  = 3
stride   = (1,1)
padding  = 1

