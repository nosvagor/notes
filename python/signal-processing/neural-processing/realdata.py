#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Creating and interpreting covariance matrices
# ### VIDEO: Python: covariance with real data
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio


# In[ ]:


# load data
matfile = sio.loadmat('sampleEEGdata')
EEG = matfile['EEG'][0,0]


## average of single-trial covariances

# specify time window (ms) for covariance matrix
tidx1 = np.argmin(np.abs(EEG['times']))
tidx2 = np.argmin(np.abs(EEG['times']-800))


# loop over trials and compute covariance for each trial
covmatT = np.zeros( (int(EEG['nbchan']),int(EEG['nbchan'])) )


for triali in range(int(EEG['trials'])):
    
    # data from this trial and time window
    tmpdat = EEG['data'][:,tidx1:tidx2,triali]
    
    # mean-center
    for ci in range(int(EEG['nbchan'])):
        tmpdat[ci,:] -= np.mean(tmpdat[ci,:])
    # covariance
    covmatT += tmpdat@tmpdat.T / (tidx2-tidx1)

# divide by N
covmatT = covmatT/EEG['trials']


# In[ ]:


## covariance of trial average

# trial average
erp = np.mean(EEG['data'][:,tidx1:tidx2,:],axis=2)

# mean-center and covariance
for ci in range(int(EEG['nbchan'])):
    erp[ci,:] -= np.mean(erp[ci,:])

covmatA = erp@erp.T / (tidx2-tidx1)


# In[ ]:


## show the covariance matrices

plt.subplot(121)
plt.pcolormesh(covmatT,vmin=-100,vmax=100)
plt.axis('square')
plt.xlabel('Channels')
plt.ylabel('Channels')
plt.title('Average of covariances')

plt.subplot(122)
plt.pcolormesh(covmatA,vmin=-100,vmax=100)
plt.axis('square')
plt.xlabel('Channels')
plt.ylabel('Channels')
plt.title('Covariance of average')

plt.tight_layout()
plt.show()

