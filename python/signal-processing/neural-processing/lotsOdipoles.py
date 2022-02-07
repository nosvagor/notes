#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Source separation with GED
# ### VIDEO: Python: Simulated EEG data with alternating dipoles
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy
import scipy
import scipy.io as sio
from pytopo import topoplotIndie
from filterFGxfun import filterFGx


# In[ ]:


## preliminary 

# mat file containing EEG, leadfield and channel locations
matfile = sio.loadmat('emptyEEG')
lf = matfile['lf'][0,0]
EEG = matfile['EEG'][0,0]

EEG['srate']  = 500
EEG['trials'] = 100
EEG['pnts']   = 1000
EEG['times']  = np.arange(0,EEG['pnts'])/EEG['srate']
EEG['data']   = np.zeros( (int(EEG['nbchan']),int(EEG['pnts']),int(EEG['trials'])) )

# scale up grid locations (convenience)
lf['GridLoc'] = lf['GridLoc']*100

nDipoles = 8 # number of distinct dipole locations

# normal dipoles (normal to the surface of the cortex)
lf_GainN = np.zeros((64,2004))
for i in range(3):
    lf_GainN += lf['Gain'][:,i,:]*lf['GridOrient'][:,i]


# In[ ]:


## pick dipoles 

# index of starting dipole location
dipoleLoc = 108

# distances to starting dipole location
locdiffs = lf['GridLoc'] - lf['GridLoc'][dipoleLoc,:]

# pick some dipole locations for the simulation
tmp = np.where( np.logical_and( np.abs(locdiffs[:,1])<.5 , np.abs(locdiffs[:,2])<.5 ) )
locs2use = np.sort(tmp)[0]

for i in range(len(locs2use)):
    zd  = lf['GridLoc'] - lf['GridLoc'][locs2use[i],:]
    ttu = np.where( np.logical_and(np.abs(zd[:,1])<.5,np.abs(zd[:,0])<.5) )[0]
    le  = np.argmax( lf['GridLoc'][ttu,2] )
    
    locs2use[i] = ttu[le]


locs2use = locs2use[1::2]
locs2use = locs2use[:nDipoles]


# In[ ]:


## plot the dipole locations and forward projections

# in a brain plot
# setup figure
fig = plt.figure()
ax  = Axes3D(fig)

# plot brain dipoles
ax.scatter(lf['GridLoc'][:,0], lf['GridLoc'][:,1], lf['GridLoc'][:,2], 'bo')
ax.scatter(lf['GridLoc'][locs2use,0], lf['GridLoc'][locs2use,1], lf['GridLoc'][locs2use,2], marker='o',s=100)
plt.title('Brain dipole locations')
plt.show()


# plot topographies
_,axs = plt.subplots(3,3,figsize=(8,8))
axs = axs.flatten()
clim  = 30
for i in range(nDipoles):
    topoplotIndie(lf_GainN[:,locs2use[i]],EEG['chanlocs'],f'Dip.#{i} proj',axs[i])

# the average
topoplotIndie(np.mean(lf_GainN[:,locs2use],axis=1),EEG['chanlocs'],'Average',axs[-1])


# In[ ]:


## create condition wave

# frequency of the dipole
freq1 = 15

# the "task activity"
taskwave = np.sin( 2*np.pi*freq1*EEG['times'] )

# center time points for windowing each dipole's activation function
centtimes = EEG['times'][np.linspace(EEG['pnts']*.1,EEG['pnts']*.9,9,dtype=np.int)]

# trials in which the waveform should be included
taskTrials = np.arange(EEG['trials']//2, EEG['trials'])


# In[ ]:


## create data

# initialize
EEG['data'] = np.zeros((EEG['nbchan'][0][0],EEG['pnts'],EEG['trials']))
sourceact = np.zeros((nDipoles,EEG['pnts'],EEG['trials']))


# loop over trials
for triali in range(EEG['trials']):
    
    # brain of noise
    dipdat = .2*np.random.randn(2004,EEG['pnts'])
    
    # insert task wave only in 2nd half of trials
    if np.in1d(triali,taskTrials):
        
        # loop through each dipole and set its activity 
        # as a delayed/windowed sine wave
        for li in range(nDipoles):
            dipdat[locs2use[li],:] = dipdat[locs2use[li],:] + taskwave * np.exp( -(EEG['times']-centtimes[li])**2/.025)

            
    # project to scalp
    EEG['data'][:,:,triali] = lf_GainN@dipdat
    
    # store dipole activation for later comparison (on your own!)
    sourceact[:,:,triali] = dipdat[locs2use,:]


# In[ ]:


## compare covariance matrices around center time points

# width of time window (in points = 400 ms window around center)
npnts = 99

# initialize covariances matrix
covmats = np.zeros((nDipoles,EEG['nbchan'][0][0],EEG['nbchan'][0][0]))

clim = 1e5
_,axs = plt.subplots(3,3,figsize=(8,8))
axs = axs.flatten()


for wini in range(nDipoles):
    
    # time window
    cidx = np.argmin(np.abs(EEG['times']-centtimes[wini]))
    
    # data around this center time point
    tmp = EEG['data'][:,cidx-npnts:cidx+npnts,:]
    tmpdat = np.reshape( tmp[:,taskTrials],(EEG['nbchan'][0][0],-1),order='F' )
    
    # covariance matrix
    covmats[wini,:,:] = np.cov(tmpdat)
    
    
    # now show the matrix
    axs[wini].imshow(covmats[wini,:,:],vmin=-clim,vmax=clim,cmap='jet')
    axs[wini].set_title(f"Covmat, time {EEG['times'][cidx]*1000:.0f} ms")
    axs[wini].set_xticks([])
    axs[wini].set_yticks([])

# average covariance matrix
axs[-1].imshow(np.mean(covmats,axis=0),vmin=-clim,vmax=clim,cmap='jet')
axs[-1].set_title("Average of covmats")
axs[-1].set_xticks([])
axs[-1].set_yticks([])
plt.show()


# In[ ]:


## GED for spatial filter

cov1 = np.zeros( (int(EEG['nbchan']),int(EEG['nbchan'])) )
cov2 = np.zeros( (int(EEG['nbchan']),int(EEG['nbchan'])) )


# covariance matrices per trial
for triali in range(int(EEG['trials'])):
    
    # data from this trial
    tdat = EEG['data'][:,:,triali]
    for ci in range(int(EEG['nbchan'])):
        tdat -= np.mean(tdat[ci,:])
    
    # add to baseline or task covariance matrix
    if np.in1d(triali,taskTrials):
        cov2 += tdat@tdat.T / EEG['pnts']
    else:
        cov1 += tdat@tdat.T / EEG['pnts']
    

# average
cov1 = cov1/ti/2
cov2 = cov2/ti/2


# GED here...
evals,evecs = scipy.linalg.eigh(cov2,cov1)
# sort according to eigenvalues
soidx = np.argsort(evals)[::-1]
evals = evals[soidx]
evecs = evecs[:,soidx]

maps = -evecs[:,:3].T @ cov2 # keep top three components


# show the eigenspectrum
plt.plot(evals,'ko-',linewidth=2,markerfacecolor='w',markersize=10)
plt.xlabel('Component number')
plt.ylabel('$\lambda$')
plt.title('Eigenspectrum')
plt.show()


# In[ ]:


# component data from three components
tmp2d = np.reshape(EEG['data'],(EEG['nbchan'][0][0],-1),order='F')
cdat  = np.reshape( evecs[:,:3].T@tmp2d, [3,EEG['pnts'],EEG['trials']],order='F' )


# plot topomaps of components
_,axs = plt.subplots(1,4,figsize=(10,5))
topoplotIndie(np.mean(lf_GainN[:,locs2use],axis=1),EEG['chanlocs'],'Ave projs',axs[0])
topoplotIndie(maps[0,:],EEG['chanlocs'],'1st comp',axs[1])
topoplotIndie(maps[1,:],EEG['chanlocs'],'2nd comp',axs[2])
topoplotIndie(maps[2,:],EEG['chanlocs'],'3rd comp',axs[3])
plt.show()


# get time series
ampts = np.zeros( (3,EEG['pnts']) )
for ci in range(3):
    fdat = filterFGx(cdat[ci,:,taskTrials],EEG['srate'],freq1,4)[0]
    hdat = scipy.signal.hilbert( fdat )
    adat = np.abs( hdat )
    ampts[ci,:] = np.mean(adat,axis=0)

plt.plot(EEG['times'],ampts.T,linewidth=3)
plt.legend(['Comp1','Comp2','Comp3'])
plt.xlabel('Time (sec.)')
plt.ylabel('Activation')
plt.title('Component amplitude time series')
plt.show()


# In[ ]:




