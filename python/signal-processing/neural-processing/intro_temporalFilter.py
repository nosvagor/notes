#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Introduction
# ### VIDEO: What are spatial filters
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:



# number of time points
n = 1000

# time vector
t = np.linspace(-2,2,n)

# create signal
s = np.zeros(n)
s[range(int(n/2)-100,int(n/2+100))] = 1
s = s + np.random.randn(n)/20

# create filter kernel
w = np.cos(2*np.pi*10*t) * np.exp( -t**2/.01 )

# filtered signal
f = np.convolve(s,w,'same')


## plotting
plt.subplot(3,1,1)
plt.plot(s)

plt.subplot(3,1,2)
plt.plot(w)

plt.subplot(3,1,3)
plt.plot(f)

plt.show()

