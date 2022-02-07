#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Convolution and transformations
# ### LECTURE: Max/mean pooling
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import torch
import torch.nn as nn


# # Create a maxpool instance

# In[ ]:


# create a pool class instance with parameters

# parameters
poolSize = 3
stride   = 3

# create the instance
p2 = nn.MaxPool2d(poolSize,stride=3)
p3 = nn.MaxPool3d(poolSize,stride=3)

# let's have a look at them
print(p2)
print(p3)


# In[ ]:


# Create image and apply maxpooling

# create a 2D and a 3D image
img2 = torch.randn(1,1,30,30)
img3 = torch.randn(1,3,30,30)


# all combinations of image and maxpool dimensionality
img2Pool2 = p2(img2)
print(f'2D image, 2D maxpool: {img2Pool2.shape}\n' )

# img2Pool3 = p3(img2)
# print(f'2D image, 3D maxpool: {img2Pool3.shape}\n' )

img3Pool2 = p2(img3)
print(f'3D image, 2D maxpool: {img3Pool2.shape}\n' )

img3Pool3 = p3(img3)
print(f'3D image, 3D maxpool: {img3Pool3.shape}\n' )


# # Create a simple CNN

# In[ ]:


littlenet = nn.Sequential(
    
    ## the conv-pool block
    nn.Conv2d(3,10,5,3,2), # convolution layer
    nn.ReLU(),             # activation function
    nn.AvgPool3d(3,3),     # average-pool
    
    ## the FFN block
    nn.Flatten(),          # vectorize to get from image to linear
    nn.Linear(588,1),      # FC linear layer
    nn.Sigmoid()           # output activation
  )


# In[ ]:


# test with a bit of data
img = torch.rand(1,3,128,128)
littlenet(img)


# In[ ]:




