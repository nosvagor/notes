#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: RNNs (and LSTM and GRU)
# ### LECTURE: The LSTM and GRU classes
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


### import libraries
import torch
import torch.nn as nn
import numpy as np


# # Explore the LSTM type

# In[ ]:


# set layer parameters
input_size  =  9 # number of features to extract (e.g., number of data channels)
hidden_size = 16 # number of units in the hidden state
num_layers  =  2 # number of vertical stacks of hidden layers (note: only the final layer gives an output)

# create an LSTM instance
lstm = nn.LSTM(input_size,hidden_size,num_layers)
lstm


# In[ ]:


# check out the source code for more detailed info about this class
get_ipython().run_line_magic('pinfo2', 'nn.LSTM')


# In[ ]:


# set data parameters
seqlength = 5
batchsize = 2

# create some data
X = torch.rand(seqlength,batchsize,input_size)

# create initial hidden states (typically initialized as zeros)
H = torch.zeros(num_layers,batchsize,hidden_size)
C = torch.zeros(num_layers,batchsize,hidden_size)

# the input is actually a tuple of (hidden,cell)
hiddeninputs = (H,C)

# run some data through the model and show the output sizes
y,h = lstm(X,hiddeninputs)
print(f' Input shape: {list(X.shape)}')
print(f'Hidden shape: {list(h[0].shape)}')
print(f'  Cell shape: {list(h[1].shape)}')
print(f'Output shape: {list(y.shape)}')


# In[ ]:


# Check out the learned parameters and their sizes
for p in lstm.named_parameters():
  if 'weight' in p[0]:
    print(f'{p[0]} has size {list(p[1].shape)}')


# In[ ]:





# # Create a DL model class

# In[ ]:


class LSTMnet(nn.Module):
  def __init__(self,input_size,num_hidden,num_layers):
    super().__init__()

    # store parameters
    self.input_size = input_size
    self.num_hidden = num_hidden
    self.num_layers = num_layers

    # RNN Layer (notation: LSTM \in RNN)
    self.lstm = nn.LSTM(input_size,num_hidden,num_layers)
    
    # linear layer for output
    self.out = nn.Linear(num_hidden,1)
  
  def forward(self,x):
    
    print(f'Input: {list(x.shape)}')

    # run through the RNN layer
    y,hidden = self.lstm(x)
    print(f'RNN-out: {list(y.shape)}')
    print(f'RNN-hidden: {list(hidden[0].shape)}')
    print(f'RNN-cell: {list(hidden[1].shape)}')
    
    # pass the RNN output through the linear output layer
    o = self.out(y)
    print(f'Output: {list(o.shape)}')

    return o,hidden


# In[ ]:


# create an instance of the model and inspect
net = LSTMnet(input_size,hidden_size,num_layers)
print(net), print(' ')

# and check out all learnable parameters
for p in net.named_parameters():
  print(f'{p[0]:>20} has size {list(p[1].shape)}')


# In[ ]:


# test the model with some data
# create some data
X = torch.rand(seqlength,batchsize,input_size)
y = torch.rand(seqlength,batchsize,1)
yHat,h = net(X)


lossfun = nn.MSELoss()
lossfun(yHat,y)


# In[ ]:





# # GRU

# In[ ]:


# create a GRU instance
gru = nn.GRU(input_size,hidden_size,num_layers)
gru


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'nn.GRU')


# In[ ]:


# create some data and a hidden state
X = torch.rand(seqlength,batchsize,input_size)
H = torch.zeros(num_layers,batchsize,hidden_size)

# run some data through the model and show the output sizes
y,h = gru(X,H) # No cell states in GRU!
print(f' Input shape: {list(X.shape)}')
print(f'Hidden shape: {list(h.shape)}')
print(f'Output shape: {list(y.shape)}')


# In[ ]:


# Check out the learned parameters and their sizes
for p in gru.named_parameters():
  print(f'{p[0]:>15} has size {list(p[1].shape)}')

