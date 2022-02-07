#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Creating and interpreting covariance matrices
# ### VIDEO: Python: Visualizing the quadratic form
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


# a happy little symmetric matrix
A = [ [1,2],[2,3] ]

# other interesting matrices to try:
#A = [ [2,1], [4,2] ]
#A = [ [2,1], [1,-1] ]
#A = [ [1,0], [0,1] ]


# range for vector w
n = 30
wRange = np.linspace(-2,2,n)

# initialize quadratic form matrix
qf = np.zeros( (len(wRange),len(wRange)) )

# compute QF
for xi in range(n):
    for yi in range(n):
        # this w
        w = np.transpose([ wRange[xi], wRange[yi] ])

        # QF
        qf[xi,yi] = np.transpose(w)@A@w / (np.transpose(w)@w)

# show the image
plt.imshow(qf,extent=[-2,2,-2,2])
# plt.show()


## an aside: the solution vectors to the normalized quadratic form
##           are the eigenvectors of the matrix.
# compute eigendecomposition
D,V = np.linalg.eig(A)

# show the eigenvectors
plt.plot( [0,V[0,0]],[0,V[1,0]]  )
plt.plot( [0,V[0,1]],[0,V[1,1]]  )
print(V)
plt.show()

