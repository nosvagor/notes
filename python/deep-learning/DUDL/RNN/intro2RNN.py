#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: RNNs (and LSTM and GRU)
# ### LECTURE: The RNN class
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


### import libraries
import torch
import torch.nn as nn
import numpy as np


# # Explore the RNN type

# In[ ]:


# set layer parameters
input_size  =  9 # number of features to extract (e.g., number of data channels)
hidden_size = 16 # number of units in the hidden state
num_layers  =  1 # number of vertical stacks of hidden layers (note: only the final layer gives an output)
actfun      = 'tanh'
bias        = True

# create an RNN instance
rnn = nn.RNN(input_size,hidden_size,num_layers,nonlinearity=actfun,bias=bias)
print(rnn)


# In[ ]:


# check out the source code for more detailed info about this class
get_ipython().run_line_magic('pinfo2', 'nn.RNN')


# In[ ]:


# set data parameters
seqlength = 5
batchsize = 2

# create some data
X = torch.rand(seqlength,batchsize,input_size)

# create a hidden layer (typically initialized as zeros)
hidden = torch.zeros(num_layers,batchsize,hidden_size)


# run some data through the model and show the output sizes
y,h = rnn(X,hidden)
print(f' Input shape: {list(X.shape)}')
print(f'Hidden shape: {list(h.shape)}')
print(f'Output shape: {list(y.shape)}')


# In[ ]:


## Default hidden state is all zeros if nothing specified:
y,h1 = rnn(X,hidden)
print(h1), print('\n\n')

y,h2 = rnn(X)
print(h2), print('\n\n')

# they're the same! (meaning default=zeros)
print(h1-h2)


# In[ ]:


# Check out the learned parameters and their sizes
for p in rnn.named_parameters():
  if 'weight' in p[0]:
    print(f'{p[0]} has size {list(p[1].shape)}')


# In[ ]:





# # Create a DL model class

# In[ ]:


class RNNnet(nn.Module):
  def __init__(self,input_size,num_hidden,num_layers):
    super().__init__()

    # store parameters
    self.input_size = input_size
    self.num_hidden = num_hidden
    self.num_layers = num_layers

    # RNN Layer
    self.rnn = nn.RNN(input_size,num_hidden,num_layers)
    
    # linear layer for output
    self.out = nn.Linear(num_hidden,1)
  
  def forward(self,x):
    
    print(f'Input: {list(x.shape)}')
    
    # initialize hidden state for first input
    hidden = torch.zeros(self.num_layers,batchsize,self.num_hidden)
    print(f'Hidden: {list(hidden.shape)}')

    # run through the RNN layer
    y,hidden = self.rnn(x,hidden)
    print(f'RNN-out: {list(y.shape)}')
    print(f'RNN-hidden: {list(hidden.shape)}')
    
    # pass the RNN output through the linear output layer
    o = self.out(y)
    print(f'Output: {list(o.shape)}')

    return o,hidden


# In[ ]:


# create an instance of the model and inspect
net = RNNnet(input_size,hidden_size,num_layers)
print(net), print(' ')

# and check out all learnable parameters
for p in net.named_parameters():
  print(f'{p[0]} has size {list(p[1].shape)}')


# In[ ]:


# test the model with some data
# create some data
X = torch.rand(seqlength,batchsize,input_size)
y = torch.rand(seqlength,batchsize,1)
yHat,h = net(X)

# try a loss function
lossfun = nn.MSELoss()
lossfun(yHat,y)


# In[ ]:





# # Additional explorations

# In[ ]:


# 1) In the video, I asked about the "l0" from the parameter name "weight_ih_l0". To explore this further, 
#    recreate that RNN instance but set the number of layers to 3. Then go through the code again to print
#    out all of the weights matrices. Refer back to the discussion of layers in the previous video. Do you 
#    understand the naming system of the weights matrices?


# In[ ]:




