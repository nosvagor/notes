#!/usr/bin/env python
# coding: utf-8

# # Code for Section 4: The discrete inverse Fourier transform
# ## This code is for learning the Fourier transform.
# 
# ### mikexcohen.com

# In[ ]:


import numpy as np
import math
import matplotlib.pyplot as plt
import pylab as pl
from IPython import display
import time as ttime
import random
from mpl_toolkits.mplot3d import Axes3D


# ---
# # VIDEO: Inverse discrete Fourier transform
# ---
# 

# In[ ]:


## first, the forward Fourier transform

# create the signal
srate  = 1000 # hz
time   = np.arange(0,2.,1/srate)  # time vector in seconds
pnts   = len(time) # number of time points
signal = 2.5 * np.sin( 2*np.pi*4*time ) + 1.5 * np.sin( 2*np.pi*6.5*time )


# prepare the Fourier transform
fourTime = np.array(np.arange(0,pnts))/pnts
fCoefs   = np.zeros(len(signal),dtype=complex)

for fi in range(0,pnts):
    
    # create complex sine wave
    csw = np.exp( -1j*2*np.pi*fi*fourTime )
    
    # compute dot product between sine wave and signal
    fCoefs[fi] = np.sum( np.multiply(signal,csw) )

# extract amplitudes
ampls = np.abs(fCoefs) / pnts
ampls[range(1,len(ampls))] = 2*ampls[range(1,len(ampls))]

# compute frequencies vector
hz = np.linspace(0,srate/2,num=math.floor(pnts/2)+1)

plt.stem(hz,ampls[range(0,len(hz))])
plt.xlim([0,10])
plt.show()


# In[ ]:


## the inverse Fourier transform

# initialize time-domain reconstruction
reconSignal = np.zeros(len(signal));

for fi in range(0,pnts):
    
    # create coefficient-modulated complex sine wave
    csw = fCoefs[fi] * np.exp( 1j*2*np.pi*fi*fourTime )
    
    # sum them together
    reconSignal = reconSignal + csw


# divide by N
reconSignal = reconSignal/pnts

plt.plot(time,signal,label='original')
plt.plot(time,np.real(reconSignal),'r.',label='reconstructed')
plt.legend()
plt.show() 

# note: signals are entire overlapping. you can try zooming in


# In[ ]:


## partial reconstruction of signal
# this differs from the MATLAB code because in-loop graphics updating 
# in python is version- and platform-dependent. Instead, here you can
# specify the proportion of frequencies to use when reconstructing the
# original time-domain signal.


# proportion of frequencies (from 0-srate) to reconstruct (.5 is Nyquist)
propfrex = .5

# set parameters
srate = 1000
time  = np.arange(0,3,1/srate)
pnts  = len(time)

# create multispectral signal
signal  = np.multiply( (1+np.sin(2*np.pi*12*time)) , np.cos(np.sin(2*np.pi*25*time)+time) )

# prepare the Fourier transform
fourTime = np.array(range(0,pnts))/pnts
fCoefs   = np.zeros(len(signal),dtype=complex)

# here is the Fourier transform...
for fi in range(0,pnts):
    csw = np.exp( -1j*2*np.pi*fi*fourTime )
    fCoefs[fi] = np.sum( np.multiply(signal,csw) ) / pnts


# frequencies in Hz (goes up to srate just as a coding trick for later visualization)
hz = np.linspace(0,srate,num=pnts)

# initialize the reconstructed signal
reconSignal = np.zeros(len(signal),dtype=complex)

# inverse Fourier transform here
for fi in range(0,pnts):#np.int(propfrex*pnts)):
    
    # create coefficient-modulated complex sine wave
    csw = fCoefs[fi] * np.exp( 1j*2*np.pi*fi*fourTime )
    
    # sum them together
    reconSignal = reconSignal + csw
    
    if fi<300 or fi>2700:
        # set up plot
        pl.cla() # wipe the figure
        plt.subplot2grid((2,1),(0,0))
        plt.plot(time,signal,label='Original')
        plt.plot(time,np.real(reconSignal),label='Reconstruction')
        plt.legend()
        
        plt.subplot2grid((2,1),(1,0))
        plt.plot(hz[0:fi],2*np.abs(fCoefs[0:fi]))
        plt.xlim([0,hz[-1]])

        # show plot
        display.clear_output(wait=True)
        display.display(pl.gcf())
        ttime.sleep(.01)


# ---
# # VIDEO: Inverse Fourier transform for signal processing
# ---
# 

# In[ ]:


## bandpass filter

# simulation params
srate = 1000
time  = np.arange(0,2-1/srate,1/srate)
pnts  = len(time)

# signal 
signal = np.sin(2*np.pi*4*time) + np.sin(2*np.pi*10*time)


# Fourier transform
fourTime = np.array(np.arange(0,pnts))/pnts
fCoefs   = np.zeros(len(signal),dtype=complex)

for fi in range(0,pnts):
    
    # create complex sine wave
    csw = np.exp( -1j*2*np.pi*fi*fourTime )
    
    # compute dot product between sine wave and signal
    fCoefs[fi] = np.sum( np.multiply(signal,csw) )/pnts


# frequencies in Hz
hz = np.linspace(0,srate/2,int(np.floor(pnts/2.0)+1))

# find the coefficient for 10 Hz
freqidx = np.argmin(np.abs(hz-10))

# set that coefficient to zero
fCoefsMod = list(fCoefs)
fCoefsMod[freqidx] = 0
# fCoefsMod[-freqidx] = 0
fCoefsMod[len(fCoefsMod)-freqidx] = 0 


# and compute inverse
reconMod = np.zeros(len(signal),dtype=complex)
for fi in range(0,pnts):
    csw = fCoefsMod[fi] * np.exp( 1j*2*np.pi*fi*fourTime )
    reconMod = reconMod + csw



# now plot
plt.plot(time,signal)
plt.title('Original signal, time domain')
plt.show()

# plot original amplitude spectrum
plt.stem(hz,2*np.abs(fCoefs[0:len(hz)]))
plt.xlim([0,25])
plt.title('Original signal, frequency domain')
plt.show()

# and plot modulated time series
plt.plot(time,np.real(reconMod))
plt.title('Band-stop filtered signal, time domain')
plt.show()


# In[ ]:


len(fCoefsMod)

