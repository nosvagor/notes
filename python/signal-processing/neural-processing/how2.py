#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Dimension reduction with PCA
# ### VIDEO: Python: How to perform a principal components analysis
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


## simulate data with covariance structure

# simulation parameters
N = 1000     # time points
M =   20     # channels

# time vector (radian units)
t = np.linspace(0,6*np.pi,N)


# relationship across channels (imposing covariance)
chanrel = np.sin(np.linspace(0,2*np.pi,M))

# create the data
data = np.outer(np.sin(t),chanrel).T + np.random.randn(M,N)

# view the data
plt.pcolormesh(data)
plt.xlabel('Time (a.u.)')
plt.ylabel('Channel')
plt.show()


# In[ ]:


## 6-step procedure for PCA

# step 1: mean-center and compute covariance matrix
for ci in range(M):
    data[ci,:] -= np.mean(data[ci,:])

covmat = data@data.T / (N-1)


# step 2: eigendecomposition
evals,evecs = np.linalg.eig( covmat )


# step 3: sort vectors by values
soidx = np.argsort(evals)
soidx = soidx[::-1]
evals = evals[soidx]
evecs = evecs[:,soidx]


# step 4: compute component time series
r = 2 # two components
comp_time_series = evecs[:,0:r].T@data

# step 5: convert eigenvalues to percent change
evals = 100*evals / np.sum(evals)


# In[ ]:


# step 6: visualize and interpret the results

# eigenvalues
plt.subplot(131)
plt.plot(evals,'s-')
plt.xlabel('Component number')
plt.ylabel('$\lambda$')

# eigenvectors
plt.subplot(132)
plt.plot(evecs[:,0:1],'s-',label=('PC1','PC2'))
plt.xlabel('Channel')
plt.ylabel('PC weight')
plt.legend()

# original channel modulator
plt.subplot(133)
plt.plot(chanrel,'s-')
plt.xlabel('Channel')
plt.ylabel('PC weight')
plt.show()

# component time series
plt.plot(comp_time_series.T)
plt.xlabel('Time (a.u.)')
plt.ylabel('Activity')
plt.legend(('PC1','PC2'))
plt.tight_layout()
plt.show()

