#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Source separation for steady-state responses
# ### VIDEO: Python: Example with real EEG data
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


# load the data

matfile = sio.loadmat('../matlab/SSVEPdata.mat')
EEG = matfile['EEG'][0,0]
EEG['srate'] = EEG['srate'][0][0]
EEG['times'] = EEG['times'][0]
EEG['data'] = np.double(EEG['data']) ## higher accuracy with double-precision data


# In[ ]:


## specify RESS parameters

# RESS parameters
ssvepfrex = [ 15, 20,   24, 17.14 ]
neig      = 1   # distance to frequency neighbors in Hz
fwhm_targ = .5  # FWHM in Hz for target
fwhm_neig = 1   # FWHM in Hz for neighbors

# shrinkage proportion
shr = .01

# time window for SSVEP
tidx = [ np.argmin(np.abs(EEG['times']--500)),np.argmin(np.abs(EEG['times']-1300)) ]

# number of time points in filter
pnts = (np.diff(tidx)+1)*EEG['trials']


# FFT param
nfft = int( EEG['srate']/.05 )
hz   = np.linspace(0,EEG['srate'],nfft)


# In[ ]:


## run RESS!
# Note: It's probably better to put some of these subroutines into Python functions,
#       but I wanted this code to match the MATLAB code as closely as possible.


_,axs = plt.subplots(4,4,figsize=(8,10))
axs = axs.flatten()


for fi in range(len(ssvepfrex)):
    
    #### S covariance matrix ####
    
    # filter
    data = copy.deepcopy(EEG['data'])
    for ti in range(int(EEG['trials'])):
        data[:,:,ti] = filterFGx(data[:,:,ti],EEG['srate'],ssvepfrex[fi],fwhm_targ)[0]
    
    # extract and mean-center data
    data = data[:,tidx[0]:tidx[1],:]
    data = np.reshape( data ,(EEG['nbchan'][0][0],-1),order='F' )
    data = data - np.mean(data,axis=1,keepdims=True)
    
    # covariance
    covS = (data@data.T) / (EEG['pnts']-1)
    
    
    #### lower 1/2 of R covariance matrix ####
    
    # filter
    data = copy.deepcopy(EEG['data'])
    for ti in range(int(EEG['trials'])):
        data[:,:,ti] = filterFGx(data[:,:,ti],EEG['srate'],ssvepfrex[fi]-neig,fwhm_neig)[0]
    
    # extract and mean-center data
    data = data[:,tidx[0]:tidx[1],:]
    data = np.reshape( data ,(EEG['nbchan'][0][0],-1),order='F' )
    data = data - np.mean(data,axis=1,keepdims=True)
    
    # covariance
    covRl = (data@data.T) / (EEG['pnts']-1)
    
    
    
    
    #### upper 1/2 of R covariance matrix ####
    
    # filter
    data = copy.deepcopy(EEG['data'])
    for ti in range(int(EEG['trials'])):
        data[:,:,ti] = filterFGx(data[:,:,ti],EEG['srate'],ssvepfrex[fi]+neig,fwhm_neig)[0]
    
    # extract and mean-center data
    data = data[:,tidx[0]:tidx[1],:]
    data = np.reshape( data ,(EEG['nbchan'][0][0],-1),order='F' )
    data = data - np.mean(data,axis=1,keepdims=True)
    
    # covariance
    covRu = (data@data.T) / (EEG['pnts']-1)
    
    
    
    # full R matrix is average of lower/upper
    covR = (covRl+covRu)/2
    
    
    
    
    #### GED with optional shrinkage
    
    # apply shrinkage to covR
    covR = (1-shr)*covR + shr*np.mean(np.linalg.eig(covR)[0])*np.eye(EEG['nbchan'][0][0])
    
    # GED and sort components
    evals,evecs = scipy.linalg.eigh(covS,covR)
    sidx  = np.argsort(evals)[::-1]
    evals = evals[sidx]
    evecs = evecs[:,sidx]
    
    # compute filter forward model and flip sign
    maps = evecs[:,0].T@covS
    maxchan = np.argmax(np.abs(maps))
    maps = maps*np.sign(maps[maxchan])
    
    
    ## component time series
    
    # compute component time series
    compts = evecs[:,0].T@np.reshape(EEG['data'],(EEG['nbchan'][0][0],-1),order='F')
    compts = np.reshape(compts,(EEG['pnts'][0][0],EEG['trials'][0][0]),order='F')

    # power spectrum averaged over trials
    powr = np.mean( np.abs(np.fft.fft(compts[tidx[0]:tidx[1],:],nfft,axis=0)/EEG['pnts'][0][0])**2 ,axis=1)
    
    
    
    #### SNR spectrum
    skipbins =  5 # .5 Hz
    numbins  = 20+skipbins  # 2 Hz
    snrSpect = np.zeros( len(powr) )

    for hzi in range(numbins,len(hz)-numbins):

        # SNR over all time points and conditions
        numer = powr[hzi]
        denom = np.mean(powr[range(hzi-numbins,hzi-skipbins)] + powr[range(hzi+skipbins,hzi+numbins)])
        snrSpect[hzi] = numer/denom
    
    
    
    ##### plotting
    axs[(fi+1)*4-4].plot(evals[:20],'s-',markerfacecolor='k',linewidth=2)
    axs[(fi+1)*4-4].set_xlabel('Component')
    axs[(fi+1)*4-4].set_ylabel('eigenspectrum')
    axs[(fi+1)*4-4].set_title(f'{ssvepfrex[fi]} Hz')
    
    # component map
    topoplotIndie(maps,EEG['chanlocs'],f'{ssvepfrex[fi]} Hz',axs[(fi+1)*4-3])
    
    # power spectrum
    axs[(fi+1)*4-2].plot(hz,powr,'k',linewidth=2)
    axs[(fi+1)*4-2].set_xlim([np.min(ssvepfrex)-5,np.max(ssvepfrex)+5])
    axs[(fi+1)*4-2].set_xlabel('Frequency (Hz)')
    axs[(fi+1)*4-2].set_ylabel('Raw power')
    axs[(fi+1)*4-2].set_title(f'{ssvepfrex[fi]} Hz')
    
    # SNR spectrum
    axs[(fi+1)*4-1].plot(hz,snrSpect,'k',linewidth=2)
    axs[(fi+1)*4-1].set_xlim([np.min(ssvepfrex)-5,np.max(ssvepfrex)+5])
    axs[(fi+1)*4-1].set_xlabel('Frequency (Hz)')
    axs[(fi+1)*4-1].set_ylabel('SNR')
    axs[(fi+1)*4-1].set_title(f'{ssvepfrex[fi]} Hz')
    
    
    

plt.tight_layout()
plt.show()


# In[ ]:




