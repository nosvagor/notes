#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Dimension reduction with PCA
# ### VIDEO: Python: Limitations of principal components analysis
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


## generate data
x = np.random.randn(1000,2)
x[:,1] *= .05

# rotation matrix
th = -np.pi/6
R1 = [ [np.cos(th),-np.sin(th)], [np.sin(th),np.cos(th)] ]
th = -np.pi/3
R2 = [ [np.cos(th),-np.sin(th)], [np.sin(th),np.cos(th)] ]

# rotate data
y = np.concatenate((x@R1,x@R2))


# plotting
plt.plot(y[:,0],y[:,1],'bo',markerfacecolor='y')
plt.axis('square')


# now PCA
y[:,0] -= np.mean(y[:,0])
y[:,1] -= np.mean(y[:,1])
evalsY,evecsY = np.linalg.eig( (y.T@y) / len(y) )

plt.plot([0,evecsY[0,0]],[0,evecsY[1,0]],'r',linewidth=3)
plt.plot([0,evecsY[0,1]],[0,evecsY[1,1]],'k',linewidth=3)

plt.show()

