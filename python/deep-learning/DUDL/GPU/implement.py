#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Running models on a GPU
# ### LECTURE: Implementation
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import time


# # Select the processor device

# In[ ]:


## Note: To run models on a GPU you must select from the menu:
#   -> Runtime
#     -> Change runtime type
#       -> Hardware accelerator
#         -> GPU


# In[ ]:


# use GPU
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)


# # Build a simple model

# In[ ]:


net = nn.Sequential(
    nn.Linear(20,100),
    nn.ReLU(),
    nn.Linear(100,500),
    nn.ReLU(),
    nn.Linear(500,30),
    nn.ReLU(),
    nn.Linear(30,2)
      )


# # Make some data

# In[ ]:


# just some random fluff
data   = torch.randn((1000,20)) # samples X features
labels = torch.randint(low=0,high=2,size=(1,1000))


# # Send the model and the data to the GPU

# In[ ]:


# model
net.to(device)

# data
data   = data.to(device)
labels = labels.to(device)


# In[ ]:


data


# In[ ]:


# you can also create data directly on the GPU
dataG = torch.randn((1000,20),device=device)
dataC = torch.randn((1000,20),device='cpu')

print(data.device)
print(dataG.device)
print(dataC.device)


# # Getting results from the model

# In[ ]:


output = net(data)


# In[ ]:


output.device


# In[ ]:


# try to plot the data
plt.plot(output.detach());

# plt.plot(output.detach().cpu());


# # Experiment: Computation time

# In[ ]:


# start the clock
starttime = time.process_time()

# move, run, retrieve
device = 'cuda:0'
net.to(device)
data   = data.to(device)
labels = labels.to(device)
output = net(data).detach().cpu()

# stop the clock
GPUtime = 1000*(time.process_time() - starttime)


# In[ ]:


# start the clock
starttime = time.process_time()

# move, run, retrieve
device = 'cpu'
net.to(device)
data   = data.to(device)
labels = labels.to(device)
output = net(data).detach().cpu()

# stop the clock
CPUtime = 1000*(time.process_time() - starttime)


# In[ ]:


# time in ms
[CPUtime,GPUtime]


# In[ ]:


# but maybe "sending" it to the CPU takes too much overhead?


# In[ ]:


# recreate network and data
net  = nn.Sequential(nn.Linear(20,100),nn.ReLU(),nn.Linear(100,500),nn.ReLU(),nn.Linear(500,30),nn.ReLU(),nn.Linear(30,2))
data = torch.randn((1000,20))

# rerun the experiment
starttime = time.process_time()
output    = net(data).detach()
CPUtime2  = 1000*(time.process_time() - starttime)

# report the results
[CPUtime2,CPUtime,GPUtime]


# In[ ]:




