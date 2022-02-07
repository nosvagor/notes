#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Source separation with GED
# ### VIDEO: Python: Complex-valued solutions
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import copy
import scipy
import scipy.io as sio
from pytopo import topoplotIndie
from filterFGxfun import filterFGx


# In[ ]:


# import the data

matfile = sio.loadmat('../matlab/lowrankEEG.mat')
EEG = matfile['EEG'][0,0]
EEG['times'] = EEG['times'][0]
# EEG['data'] = np.double(EEG['data'])


# In[ ]:


# rank of data

r = np.linalg.matrix_rank(EEG['data'][:,:,0])

print('Rank = ' + str(r))


# In[ ]:


# filter data in alpha
centerFreq = 11
freqFWHM = 4

fdata = copy.deepcopy(EEG['data'])
for ti in range(int(EEG['trials'])):
    tmdat = EEG['data'][:,:,ti]
    fdata[:,:,ti] = filterFGx(tmdat,EEG['srate'][0][0],centerFreq,freqFWHM)[0]

    
# covariance matrices
covR = np.zeros( (EEG['nbchan'][0][0],EEG['nbchan'][0][0]) )
covS = np.zeros( (EEG['nbchan'][0][0],EEG['nbchan'][0][0]) )

for ti in range(EEG['trials'][0][0]):
    
    # covariance of broadband
    covR += np.cov(EEG['data'][:,:,ti])
    
    # covariance of post-stim period
    covS += np.cov(fdata[:,:,ti])
    
# average covariances by dividing by trials
covR = covR/ti
covS = covS/ti


# In[ ]:


## regularized GED

# regularization amount
regu_gam = .0

# apply regularization
R = (1-regu_gam)*covR + regu_gam*np.mean(np.linalg.eig(covR)[0])*np.eye(EEG['nbchan'][0][0])

# report ranks of matrices
print('rank(S)  = ' + str(np.linalg.matrix_rank(covS)))
print('rank(R)  = ' + str(np.linalg.matrix_rank(covR)))
print('rank(Rr) = ' + str(np.linalg.matrix_rank(R)))


# In[ ]:


### GED

evals,evecs = scipy.linalg.eigh(covS,R)
# sort according to eigenvalues
soidx = np.argsort(evals)[::-1]
evals = evals[soidx]
evecs = evecs[:,soidx]

# component time series
tmpts = evecs[:,0].T @ np.reshape(EEG['data'],(EEG['nbchan'][0][0],-1),order='F')
ts = np.reshape( tmpts,(EEG['pnts'][0][0],EEG['trials'][0][0]),order='F' )
             
# topomaps and time series
topo = evecs[:,0].T@covS
mv = np.argmax(np.abs(topo))
if topo[mv]<0:
    topo = -topo
    ts = -ts


# In[ ]:


## some plotting

# topoplot of component map
topoplotIndie(topo,EEG['chanlocs'],'Component map')
plt.show()

# ERP
plt.plot(EEG['times'],np.mean(ts,axis=1),'k',linewidth=3)
plt.xlim([-200, 1000])
plt.xlabel('Time (ms)')
plt.show()


# In[ ]:




