#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Independent components analysis
# ### VIDEO: Data distributions and ICA
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

# ICA algorithm, taken from https://github.com/camilleanne/pulse/blob/master/jade.py
# I made a few tiny adjustments.
import jade


# In[ ]:


## some simple data

N = 1000

# a non-Gaussian distribution
dist1 = np.random.rand(N)

# another non-Gaussian distribution
dist2 = np.random.rand(N)**2

# their separate and combined distributions
_,axs = plt.subplots(1,2)
axs[0].hist(dist1,100)
axs[0].set_title('Distribution 1')

axs[1].hist(dist2,100)
axs[1].set_title('Distribution 1')
plt.tight_layout()
plt.show()

# and their summed distribution
plt.hist(dist1,100)
plt.title('Distributions 1+2')
plt.xlabel('Data value')
plt.ylabel('Count')
plt.show()

# QUESTION: What is the shape of the combined distribution? 
#           Are you surprised at the result?
#           What does this tell you about mixing distributions?


# In[ ]:


## ICA on a trivial example (unmixed data)

data = np.zeros( (2,N) )

# two non-Gaussian distributions
data[0,:] = np.random.rand(N)
data[1,:] = np.random.rand(N)**4

# ICA and scores
b = jade.main(data)[0]
iscores = np.array(b)@data



#### plot distributions
_,axs = plt.subplots(2,2)
# data 1
axs[0,0].hist(data[0,:],100)
axs[0,0].set_title('Data 1')

# data 1
axs[0,1].hist(data[1,:],100)
axs[0,1].set_title('Data 1')

# ICs 1
axs[1,0].hist(iscores[0,:],100)
axs[1,0].set_title('IC 1')

# ICs 2
axs[1,1].hist(iscores[1,:],100)
axs[1,1].set_title('IC 2')

plt.tight_layout()
plt.show()


# In[ ]:


# now plot data as a function of ICs

_,axs = plt.subplots(1,2)
axs[0].plot(data[0,:],iscores[0,:],'o')
axs[0].set_xlabel('Data')
axs[0].set_ylabel('IC1 scores')

axs[1].plot(data[1,:],iscores[1,:],'o')
axs[1].set_xlabel('Data')
axs[1].set_ylabel('IC1 scores')

plt.tight_layout()
plt.show()


# In[ ]:




