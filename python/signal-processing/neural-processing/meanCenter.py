#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Dimension reduction with PCA
# ### VIDEO: Python: Importance of mean-centering for PCA
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


## create data
x = np.random.randn(1000,2) 
x[:,1] = .2*x[:,1]

# rotation matrix
th = -np.pi/4
R1 = [ [np.cos(th),-np.sin(th)], [np.sin(th),np.cos(th)] ]

# rotate data to induce correlation
y = x@R1


### add a mean offset ###
y[:,0] = y[:,0] + 1


# PCA of y (correlated data)
covmat = y.T@y / (len(y)-1)
evals,evecs = np.linalg.eig(covmat)

# (optional) mean-center the data for display
# y[:,0] -= np.mean(y[:,0])
# y[:,1] -= np.mean(y[:,1])


# plot the data in a scatter plot
plt.plot(y[:,0],y[:,1],'mo')

# plot the eigenvectors
plt.plot([0,evecs[0,0]],[0,evecs[1,0]],'k')
plt.plot([0,evecs[0,1]],[0,evecs[1,1]],'k')

plt.axis('square')
plt.show()

