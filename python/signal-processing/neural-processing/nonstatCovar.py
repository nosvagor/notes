#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Source separation with GED
# ### VIDEO: Python: GED with nonstationary covariances
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import scipy
import scipy.io as sio
import matplotlib.pyplot as plt


# In[ ]:


## simulate data with covariance structure

# simulation parameters
N = 500     # time points per covariance matrix
M =  20     # channels

# time vector (radian units)
t = np.linspace(0,6*np.pi,N)


# relationship across channels (imposing covariance)
chanrel1 = np.random.randn(M)
chanrel2 = np.sin(np.linspace(0,2*np.pi,M))
chanrel3 = np.exp( -np.linspace(-2,2,M)**2 )


# create the data segments
data1 = np.outer(np.sin(t + np.random.rand()*2*np.pi),chanrel1).T + np.random.randn(M,N)
data2 = np.outer(np.sin(t + np.random.rand()*2*np.pi),chanrel2).T + np.random.randn(M,N)
data3 = np.outer(np.sin(t + np.random.rand()*2*np.pi),chanrel3).T + np.random.randn(M,N)


# view the data
alldata = np.hstack((data1,data2,data3))
alldata.shape

fig = plt.figure(figsize=(6,4))
for i in range(M):
    plt.plot(alldata[i,:]+i*3,linewidth=.4)
plt.xlabel('Time (rad.)')
plt.ylabel('Channel')
plt.yticks([])
plt.xlim([0,1500])
plt.show()


# In[ ]:


## covariance matrices of the three windows

# covariances of separate data segments
covm1 = np.cov(data1)
covm2 = np.cov(data2)
covm3 = np.cov(data3)

# covariance of the 2nd and 3rd data chunks
covm23 = np.cov( np.hstack((data2,data3)) )


# plot the covariance matrices
clim = .5

_,axs = plt.subplots(2,2,figsize=(8,6))
axs[0,0].imshow(covm1,vmin=-clim,vmax=clim)
axs[0,0].set_xticks([])
axs[0,0].set_xlabel('Channels')
axs[0,0].set_ylabel('Channels')
axs[0,0].set_title('Data 1')

axs[0,1].imshow(covm2,vmin=-clim,vmax=clim)
axs[0,1].set_xticks([])
axs[0,1].set_xlabel('Channels')
axs[0,1].set_ylabel('Channels')
axs[0,1].set_title('Data 2')

axs[1,0].imshow(covm3,vmin=-clim,vmax=clim)
axs[1,0].set_xticks([])
axs[1,0].set_xlabel('Channels')
axs[1,0].set_ylabel('Channels')
axs[1,0].set_title('Data 3')

axs[1,1].imshow(covm23,vmin=-clim,vmax=clim)
axs[1,1].set_xticks([])
axs[1,1].set_xlabel('Channels')
axs[1,1].set_ylabel('Channels')
axs[1,1].set_title('Data 2&3')

plt.tight_layout()
plt.show()


# In[ ]:


## GED relative to the first time window

D2,V2 = scipy.linalg.eigh(covm2,covm1)
sidx  = np.argsort(D2)[::-1]
D2 = D2[sidx]
V2 = V2[:,sidx]

D3,V3 = scipy.linalg.eigh(covm3,covm1)
sidx  = np.argsort(D3)[::-1]
D3 = D3[sidx]
V3 = V3[:,sidx]

D23,V23 = scipy.linalg.eigh(covm23,covm1)
sidx    = np.argsort(D23)[::-1]
D23 = D23[sidx]
V23 = V23[:,sidx]


# In[ ]:


## plot the filter forward models

# axis limits to make plots comparable
maxy = 6.5
ylim = [-2,2]


_,axs = plt.subplots(2,3,figsize=(8,5))


## period 2 vs. baseline
axs[0,0].plot(D2,'ks-',markerfacecolor='w',markersize=10)
axs[0,0].set_xlabel('Component number')
axs[0,0].set_ylabel('$\lambda$')
axs[0,0].set_ylim([0,maxy])
axs[0,0].set_title('GED: 2 vs 1')

axs[1,0].plot(V2[:,0].T@covm2,'ks-',markerfacecolor='w',markersize=10,label='Filter')
axs[1,0].plot(chanrel2,'ro-',markerfacecolor='w',markersize=10,label='Simulated')
axs[1,0].set_ylim(ylim)
axs[1,0].set_xlabel('Channel')
axs[1,0].set_ylabel('Weight')
axs[1,0].set_title('Filter forward model')
axs[1,0].legend()



## period 3 vs. baseline
axs[0,1].plot(D3,'ks-',markerfacecolor='w',markersize=10)
axs[0,1].set_xlabel('Component number')
axs[0,1].set_ylabel('$\lambda$')
axs[0,1].set_ylim([0,maxy])
axs[0,1].set_title('GED: 3 vs 1')

axs[1,1].plot(V3[:,0].T@covm3,'ks-',markerfacecolor='w',markersize=10,label='Filter')
axs[1,1].plot(chanrel3,'ro-',markerfacecolor='w',markersize=10,label='Simulated')
axs[1,1].set_ylim(ylim)
axs[1,1].set_xlabel('Channel')
axs[1,1].set_ylabel('Weight')
axs[1,1].set_title('Filter forward model')
axs[1,1].legend()



## periods 2&3 vs. baseline
axs[0,2].plot(D23,'ks-',markerfacecolor='w',markersize=10)
axs[0,2].set_xlabel('Component number')
axs[0,2].set_ylabel('$\lambda$')
axs[0,2].set_ylim([0,maxy])
axs[0,2].set_title('GED: 2&3 vs 1')

axs[1,2].plot(V23[:,0].T@covm23,'ks-',markerfacecolor='w',markersize=10,label='Filter 1')
axs[1,2].plot(V23[:,1].T@covm23,'bs-',markerfacecolor='w',markersize=10,label='Filter 2')
axs[1,2].set_ylim(ylim)
axs[1,2].set_xlabel('Channel')
axs[1,2].set_ylabel('Weight')
axs[1,2].set_title('Filter forward model')
axs[1,2].legend()



plt.tight_layout()
plt.show()


# In[ ]:




