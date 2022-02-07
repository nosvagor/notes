#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Dimension reduction with PCA
# ### VIDEO: Python: PCA via SVD of covariance
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import copy


# In[ ]:


## simulate data with covariance structure

# simulation parameters
N = 10000    # time points
M =    20    # channels

# time vector (radian units)
t = np.linspace(0,6*np.pi,N)

# relationship across channels (imposing covariance)
chanrel = np.sin(np.linspace(0,2*np.pi,M))

# create the data
data = np.outer(np.sin(t),chanrel).T + np.random.randn(M,N)

# view the data
plt.pcolormesh(data)
plt.xlabel('Time (rad.)')
plt.ylabel('Channel')
plt.show()


# In[ ]:


## PCA via eigendecomposition of covariance matrix

# step 1: mean-center and compute covariance matrix
dataM = copy.deepcopy(data)
for ci in range(M):
    dataM[ci,:] -= np.mean(dataM[ci,:])

covmat = dataM@dataM.T / (N-1)


# step 2: eigendecomposition
evals,evecs = np.linalg.eig( covmat )


# step 3: sort vectors by values
soidx = np.argsort(evals)
soidx = soidx[::-1]
evals = evals[soidx]
evecs = evecs[:,soidx]

# step 5: convert eigenvalues to percent change
evals = 100*evals / np.sum(evals)

# step 4: compute component time series
eig_ts = evecs[:,0].T@data


# In[ ]:


## PCA via SVD of data matrix

U,s,V = np.linalg.svd( data,'econ' )

print('U: '+str(np.shape(U)))
print('s: '+str(np.shape(s)))
print('V: '+str(np.shape(V)))

# convert singular values to %
S = s**2; # makes it comparable to eigenvalues
S = 100*S / np.sum(S)


# In[ ]:


## show the results

# plot eigenvalue/singular-value spectrum
plt.subplot(121)
plt.plot(evals,'bs-',label='eigenvalues')
plt.plot(S,'ro-',label='singular vals.')
plt.xlabel('Component number')
plt.ylabel('$\lambda$ or $\sigma$')
plt.legend()
plt.title('Eigenspectrum')


# show eigenvector/singular value
plt.subplot(122)
plt.plot(evecs[:,0],'bs-',label='eig vector')
plt.plot(U[:,0],'ro-',label='singular vect.')
plt.xlabel('Vector component')
plt.ylabel('Weight')
plt.legend()
plt.title('Component weights')

plt.show()


# time series
timevec = np.arange(0,N)/N
plt.plot(timevec,V[0,:]*s[0],'.',label='from svd')
plt.plot(timevec,eig_ts,label='from eig')
plt.xlabel('Time (norm.)')
plt.title('Component time series')
plt.legend()
# plt.xlim([.2,.23])
plt.show()

