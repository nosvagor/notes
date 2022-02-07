#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Linear algebra crash course
# ### VIDEO: Python: Inverse and AtA (SOLUTIONS file)
# #### Instructor: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# 
# ---
# # Matrix inverse
# ---
# 

# In[ ]:


# size of square matrix
m = 3

# generate random matrix
A = np.random.randn(m,m)

# compute its inverse
Ainv = np.linalg.inv(A)

# and check the multiplication
idm = A@Ainv

# print the matrix. Note the computer rounding errors on the off-diagonals
print(idm)
# print( np.round(idm,4) ) # try this instead ;)


# In[ ]:


# show in an image
plt.subplot(131)
plt.imshow(A)
plt.title('Matrix A')

plt.subplot(132)
plt.imshow(Ainv)
plt.title('Matrix $A^{-1}$')

plt.subplot(133)
plt.imshow(idm)
plt.title('AA$^{-1}$')

plt.show()


# what happens when you try it with a reduced-rank matrix?
A = np.random.randn(4,2) @ np.random.randn(2,4)


# In[ ]:


### The left inverse

# m>n for left inverse,
# m<n for right inverse
m = 6
n = 3

# create matrices
A = np.random.randn(m,n)
AtA = A.T@A
AAt = A@A.T

# inspect ranks
print('Shape of A^TA:', np.shape(AtA) )
print('Rank of A^TA:', np.linalg.matrix_rank(AtA) )
print('Shape of AA^T:', np.shape(AAt) )
print('Rank of AA^T:', np.linalg.matrix_rank(AAt) ) 

# left inverse
Aleft = np.linalg.inv(AtA)@A.T

# now test!
I_left  = Aleft  @ A

print(I_left), print(' ')


# and then test using the inverse function
AtA_inv = np.linalg.inv(AtA)
I_AtA   = AtA_inv @ AtA

AAt_inv = np.linalg.inv(AAt)
I_AAt   = AAt_inv @ AAt

print(I_AtA), print(' ')
print(I_AAt)


# In[ ]:


## show images
plt.subplot(331)
plt.imshow(A), plt.axis('off')
plt.title('A')

plt.subplot(332)
plt.imshow(AtA), plt.axis('off')
plt.title('A$^T$A')

plt.subplot(333)
plt.imshow(AAt), plt.axis('off')
plt.title('AA$^T$')

plt.subplot(335)
plt.imshow(Aleft), plt.axis('off')
plt.title('$(A^TA)^{-1}A^T$')

plt.subplot(338)
plt.imshow(I_left), plt.axis('off')
plt.title('[ $(A^TA)^{-1}A^T ]$  A')

plt.show()


# In[ ]:


## Right inverse

# Copy/paste the code from above and adapt to the right inverse!


# In[ ]:





# ---
# # The wonderful matrix AtA
# ---

# In[ ]:


# show that AtA is square

# sizes
m = 6
n = 3

# create a random matrix
A = np.random.randn(m,n)

# compute it both ways
AtA = A.T@A
AAt = A@A.T

print(AtA.shape)
print(AAt.shape)


# In[ ]:


## show that it's symmetric

_,axs = plt.subplots(2,3,figsize=(6,4))

# show the matrices
axs[0,0].imshow(A)
axs[0,0].set_title('A')

axs[0,1].imshow(AtA)
axs[0,1].set_title('A$^T$A')

axs[0,2].imshow(AtA-AtA.T)
axs[0,2].set_title('A$^T$A  -  (A$^T$A)$^T$')


axs[1,0].imshow(A)
axs[1,0].set_title('A')

axs[1,1].imshow(AAt)
axs[1,1].set_title('AA$^T$')

axs[1,2].imshow(AAt-AAt.T)
axs[1,2].set_title('AA$^T$  -  (AA$^T$)$^T$')


plt.tight_layout()
plt.show()


# In[ ]:




