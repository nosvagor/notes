#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Understand and design CNNs
# ### LECTURE: CodeChallenge: Custom loss functions
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

import matplotlib.pyplot as plt
from IPython import display
display.set_matplotlib_formats('svg')


# # Create Gaussian blurs with varying widths and occluding bars

# In[ ]:


nGauss  = 1000
imgSize = 91

x = np.linspace(-4,4,imgSize)
X,Y = np.meshgrid(x,x)

# vary the weights smoothly
widths = np.linspace(2,20,nGauss)

# initialize tensor containing images
images = torch.zeros(nGauss,1,imgSize,imgSize)

for i in range(nGauss):

  # create the gaussian with random centers
  ro = 1.5*np.random.randn(2) # ro = random offset
  G  = np.exp( -( (X-ro[0])**2 + (Y-ro[1])**2) / widths[i] )
  
  # and add noise
  G  = G + np.random.randn(imgSize,imgSize)/5

  # add a random bar randomly
  i1 = np.random.choice(np.arange(2,28))
  i2 = np.random.choice(np.arange(2,6))
  if np.random.randn()>0:
    G[i1:i1+i2,] = 1
  else:
    G[:,i1:i1+i2] = 1
  
  # add to the tensor
  images[i,:,:,:] = torch.Tensor(G).view(1,imgSize,imgSize)


# In[ ]:


# visualize some images
fig,axs = plt.subplots(3,7,figsize=(10,5))

for i,ax in enumerate(axs.flatten()):
  whichpic = np.random.randint(nGauss)
  G = np.squeeze( images[whichpic,:,:] )
  ax.imshow(G,vmin=-1,vmax=1,cmap='jet')
  ax.set_xticks([])
  ax.set_yticks([])

plt.show()


# # Custom loss functions

# In[ ]:


# L1 loss function

class myL1Loss(nn.Module):
  def __init__(self):
    super().__init__()
      
  def forward(self,yHat,y):
    l = torch.mean( torch.abs(yHat-y) )
    return l


# In[ ]:


# L2+average loss function

class myL2AveLoss(nn.Module):
  def __init__(self):
    super().__init__()
      
  def forward(self,yHat,y):
    # MSE part
    l = torch.mean( (yHat-y)**2 )

    # average part
    a = torch.abs(torch.mean(yHat))

    # sum together
    return l + a


# In[ ]:


# correlation loss function

class myCorLoss(nn.Module):
  def __init__(self):
    super().__init__()
      
  def forward(self,yHat,y):
    
    meanx = torch.mean(yHat)
    meany = torch.mean(y)

    num = torch.sum( (yHat-meanx)*(y-meany) )
    den = (torch.numel(y)-1) * torch.std(yHat) * torch.std(y)
    return -num/den


# # Create the DL model

# In[ ]:


# create a class for the model
def makeTheNet():

  class gausnet(nn.Module):
    def __init__(self):
      super().__init__()
      
      # encoding layer
      self.enc = nn.Sequential(
          nn.Conv2d(1,6,3,padding=1),
          nn.ReLU(),
          nn.MaxPool2d(2,2),
          nn.Conv2d(6,4,3,padding=1),
          nn.ReLU(),
          nn.MaxPool2d(2,2)  
          )
      
      # decoding layer
      self.dec = nn.Sequential(
          nn.ConvTranspose2d(4,6,3,2),
          nn.ReLU(),
          nn.ConvTranspose2d(6,1,3,2),
          )
      
    def forward(self,x):
      return self.dec( self.enc(x) )
  
  # create the model instance
  net = gausnet()
  
  # loss functions (leave one uncommented!)
  # lossfun = nn.MSELoss()
  lossfun = myL1Loss()
  # lossfun = myL2AveLoss()
  # lossfun = myCorLoss()

  # optimizer
  optimizer = torch.optim.Adam(net.parameters(),lr=.001)

  return net,lossfun,optimizer


# # Create a function that trains the model

# In[ ]:


# a function that trains the model

def function2trainTheModel():

  # number of epochs
  numepochs = 1000
  
  # create a new model
  net,lossfun,optimizer = makeTheNet()

  # initialize losses
  losses = torch.zeros(numepochs)

  # loop over epochs
  for epochi in range(numepochs):

    # pick a set of images at random
    pics2use = np.random.choice(nGauss,size=32,replace=False)
    X = images[pics2use,:,:,:]

    # forward pass and loss
    yHat = net(X)
    loss = lossfun(yHat,X)
    losses[epochi] = loss.item()

    # backprop
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

  # end epochs

  # function output
  return losses,net


# # Run the model and show the results!

# In[ ]:


# train the model!
losses,net = function2trainTheModel()


# In[ ]:


plt.plot(losses,'s-',label='Train')
plt.xlabel('Epochs')
plt.ylabel('Loss function')
plt.title('Model loss (final loss=%.3f)'%losses[-1])

plt.show()


# In[ ]:


# visualize some images

pics2use = np.random.choice(nGauss,size=32,replace=False)
X = images[pics2use,:,:,:]
yHat = net(X)

fig,axs = plt.subplots(2,10,figsize=(18,4))

for i in range(10):
  
  G = torch.squeeze( X[i,0,:,:] ).detach()
  O = torch.squeeze( yHat[i,0,:,:] ).detach()
  
  axs[0,i].imshow(G,vmin=-1,vmax=1,cmap='jet')
  axs[0,i].axis('off')
  axs[0,i].set_title('Input ($\mu$=%.2f)'%torch.mean(G).item(),fontsize=10)

  axs[1,i].imshow(O,vmin=-1,vmax=1,cmap='jet')
  axs[1,i].axis('off')
  axs[1,i].set_title('Output ($\mu$=%.2f)'%torch.mean(O).item(),fontsize=10)

plt.show()


# In[ ]:





# # Additional explorations

# In[ ]:


# 1) The code in this notebook requires "manually" switching between loss functions by (un)commenting. Modify the
#    code so that you can list the name of the loss function as an input to makeTheNet().
# 
# 2) Here's an interesting loss function: minimize the variance of the model's output. Don't worry about comparing
#    to the input image; just set the loss function to be the variance of the output. What do the results look like,
#    and why does this happen?
# 
# 3) What if L2 minimization (MSE) is more important than average minimization? Modify the L2LossAve class so that the
#    average has a weaker influence compared to the L2 loss.
# 
# 
# Reminder: This codeChallenge was designed to be a fun exercise to introduce you to the mechanics of creating and using
#           custom-built loss functions. The PyTorch built-in MSELoss is actually the best one to use for autoencoders
#           in most cases.
# 

