#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math
import matplotlib.pyplot as plt
import random
import timeit
import scipy.fftpack
from mpl_toolkits.mplot3d import Axes3D


# 
# ---
# # VIDEO: Sampling theorem
# ---
# 

# In[ ]:


# create the signal
srate  = 1000
pnts   = 1000
signal = np.random.randn(pnts)


# The loop of the Fourier transform (although we're not computing it)
#for fi in range(0,pnts):
    #csw = np.exp( -1i*2*np.pi*fi*fourTime )
    #fCoefs[fi] = np.sum( np.multiply(signal,csw) ) / pnts


# compute frequencies vector
hz = np.linspace(0,srate/2,int(np.floor(pnts/2)+1))

# compute frequency resolution
freqres = np.mean(np.diff(hz))

# print result in command window
print('Frequency resolution is',freqres,'Hz')


# In[ ]:


# parameters (try adjusting the srate!)
srate  = 10
time   = np.arange(0,2,1/srate)

# create signal
signal = np.zeros(len(time))
signal[0:np.int(np.round(len(time)*.1))] = 1

# spectrum and frequencies vector
signalX = scipy.fftpack.fft(signal)
hz = np.linspace(0,srate,len(time)) # plotting trick... frequencies really only go up to Nyquist

# plot
plt.plot(time,signal,'s-')
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude')
plt.title('Time domain')
plt.show()

plt.plot(hz,2*abs(signalX),'s-')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency domain')
plt.show()


# 
# ---
# # VIDEO: Time-domain zero padding
# ---
# 

# In[ ]:


# create the signal
signal = np.hanning(40)

# note: in MATLAB I have a separate cell for the manual zero-padding.
#       Here you can just uncomment the following line.
#signal = np.concatenate((signal,np.zeros(len(signal))),axis=0)

# time the fast Fourier transform
signalX = scipy.fftpack.fft(signal)

# extract amplitude
ampl = np.abs(signalX)

# normalized frequency units
frequnits = np.linspace(0,1,len(signal))

# and plot
plt.plot(signal,'ks-')
plt.xlim(0,80)
plt.xlabel('Time (a.u.)')
plt.ylabel('Amplitude')
plt.title('Time domain')
plt.show()

plt.stem(frequnits,ampl)
plt.xlim(-.01,.3)
plt.xlabel('Frequency (a.u.)')
plt.ylabel('Amplitude')
plt.title('Frequency domain')
plt.show()


# In[ ]:


## zero-padding in fft function

# create the signal
signal = [ 4, 6, -1, 0, 5, -4 ]

# number of zeros to add after signal
n2pad = [ 0, 10, 100 ]

for zi in range(0,len(n2pad)):
    
    # total length of signal
    zeropadN = len(signal)+n2pad[zi]
    
    # FFT and amplitude
    sigampl   = np.abs( scipy.fftpack.fft(signal,zeropadN) )
    
    # one of the two normalization steps
    sigampl = sigampl / 1
    
    frequnits = np.linspace(0,1,zeropadN+1)
    
    # and plot
    plt.plot(frequnits[:-1],sigampl,'s-',label='%g-point FFT' %zeropadN)


# add some plot extras
plt.legend()
plt.xlabel('Frequency (.5 = Nyquist)')
plt.ylabel('Amplitude (a.u.)')
plt.show()


# 
# ---
# # VIDEO: Frequency-domain zero padding
# ---
# 

# In[ ]:


# create the signal
signal = [ 4, 6, -1, 0, 5, -4 ]

# fft
signalX = scipy.fftpack.fft(signal)
    
# number of zeros to add after spectrum
n2pad = [ 0, 10, 100 ]

for zi in range(len(n2pad)):
    
    # spectral zero-padding
    zeropadN = len(signal)+n2pad[zi]
    
    # reconstruction via ifft
    reconSig = scipy.fftpack.ifft(signalX,zeropadN) * zeropadN
    normtime = np.linspace(0,1,len(reconSig))
    
    # and plot
    plt.plot(normtime,np.real(reconSig),'s-',label='%g-point FFT' %zeropadN)

# add some plot extras
plt.legend()
plt.xlabel('Time (norm.)')
plt.show()


# In[ ]:


## Another example

# create the signal
srate  = 1000
x      = np.array(range(0,256))/srate
signal = np.sin(2*np.pi*20*x)>.3

# number of zeros to add after spectrum
n2pad = [ 1, 2, 5 ]

# line colors
colors = 'krb'

# setup axis
fig,ax = plt.subplots(2,1,figsize=(10,7))

for zi in range(len(n2pad)):
    
    # fft
    signalX = scipy.fftpack.fft(signal)
    
    # spectral zero-padding
    zeropadN = 2**math.ceil(math.log(len(signal)*n2pad[zi],2))
    
    # reconstruction via ifft
    reconSig = scipy.fftpack.ifft(signalX,zeropadN) * zeropadN
    normtime = np.linspace(x[0],x[-1],len(reconSig)) # new time vector
    srateNew = 1/np.mean(np.diff(normtime)) # new sampling rate
    
    # power spectrum
    ampl = np.abs(scipy.fftpack.fft( np.real(reconSig) ))
    hz   = np.linspace(0,srateNew/2,np.int(np.floor(len(reconSig)/2+1)))
    
    ax[0].plot(normtime,np.real(reconSig),label='%g-point IFFT' %zeropadN,color=colors[zi])
    
    # plot amplitude spectrum
    ax[1].plot(hz,ampl[0:len(hz)])


# add some plot extras
ax[0].set_xlabel('Time (sec.)')
ax[0].set_title('Time domain')
# ax[0].set_xlim([.01,.1]) # optional zooming in

ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('Amplitude (non-normalized)')
ax[1].set_title('Frequency domain')
plt.show()


# 
# ---
# # VIDEO: Sampling rate vs. signal length
# ---
# 

# In[ ]:


## difference between sampling rate and number of time points for Fourier frequencies

# temporal parameters
srates  = [100, 100, 1000]
timedur = [  1,  10,    1]
freq    = 5 # in Hz, for the signal


# setup plotting
fig,ax = plt.subplots(2,1,figsize=(10,9))
colors  = 'kmb'
symbols = 'op.'
legendText = [0]*len(srates)


for parami in range(len(srates)):
    
    # define sampling rate in this round
    srate = srates[parami] # in Hz
    
    # define time
    time = np.arange(-1,timedur[parami],1/srate)
    
    # create signal (Morlet wavelet)
    signal = np.multiply( np.cos(2*np.pi*freq*time) , np.exp( (-time**2) / .05 ) )
    
    # compute FFT and normalize
    signalX = scipy.fftpack.fft(signal)
    signalX = signalX/np.max(signalX)
    
    # define vector of frequencies in Hz
    hz = np.linspace(0,srate/2,int(np.floor(len(signal)/2)+1))
    
    # plot time-domain signal
    ax[0].plot(time,signal,color=colors[parami],marker=symbols[parami])
    
    # plot frequency-domain signal
    ax[1].plot(hz,np.abs(signalX[0:len(hz)]),color=colors[parami],marker=symbols[parami])
    
    # legend text
    legendText[parami] = f'srate={srates[parami]}, N={timedur[parami]+1} s'


ax[0].set_xlim([-1,1])
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Time domain')
ax[0].legend(legendText)

ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('Amplitude')
ax[1].set_title('Frequency domain')
ax[1].legend(legendText)

plt.show()

