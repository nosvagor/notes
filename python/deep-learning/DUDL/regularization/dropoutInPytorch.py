#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Regularization
# ### LECTURE: Dropout regularization in practice
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import torch
import torch.nn as nn
import torch.nn.functional as F


# # Using dropout

# In[ ]:


# define a dropout instance and make some data
prob = .5

dropout = nn.Dropout(p=prob)
x = torch.ones(10)

# let's see what dropout returns
y = dropout(x)
print(x)
print(y*(1-prob))
print(torch.mean(y))


# In[ ]:


# dropout is turned off when evaluating the model
dropout.eval()
y = dropout(x)
print(y)
print(torch.mean(y))


# In[ ]:


# annoyingly, F.dropout() is not deactivated in eval mode:

dropout.eval()
y = F.dropout(x)
print(y)
print(torch.mean(y))


# In[ ]:


# but you can manually switch it off
# dropout.eval()
y = F.dropout(x,training=False)

print(y)
print(torch.mean(y))


# In[ ]:


# the model needs to be reset after toggling into eval mode

dropout.train()
y = dropout(x)
print(y) # with dropout


dropout.eval()
y = dropout(x)
print(y) # without dropout


# dropout.train()
y = dropout(x)
print(y) # still w/o dropout ;)


# In[ ]:




