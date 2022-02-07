#!/usr/bin/env python
# coding: utf-8

# # COURSE: PCA and multivariate neural signal processing
# ## SECTION: Linear algebra crash course
# ### VIDEO: Python: Eigendecomposition and SVD (SOLUTIONS file)
# #### Instructor: sincxpress.com

# In[ ]:


# import libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# 
# ---
# # Eigendecomposition
# ---
# 

# In[ ]:



# This cell shows a geometric picture of eigenvectors in 2D.
#  Notice that the two red lines (v and Av) are collinear, 
#  but not the two black lines (w and Aw). v is an eigenvector, w is not.



# matrix
A = [ [1,5], [2,4] ]

# extract the eigenvalues
eigvals = np.linalg.eig(A)

# note that the eigenvalues are in the first element of eigvals:
print(eigvals[0])


# specify two vectors
v1 = np.array([ 1,1 ])    # is an eigenvector!
v2 = np.random.randn(2,1) # unlikely to be an eigenvector
v2 = v2/np.linalg.norm(v2)# unit length for convenience

# compute Av
Av1 = A@v1
Av2 = A@v2


# plot the vectors and Av
plt.plot([0,v1[0]] ,[0,v1[1]],'r')
plt.plot([0,Av1[0]],[0,Av1[1]],'r--')
plt.plot([0,v2[0]] ,[0,v2[1]],'k')
plt.plot([0,Av2[0]],[0,Av2[1]],'k--')

plt.axis([-8,8,-8,8])
plt.show()


# QUESTION: Is there something special about vector v? To find out,
#           change one value of matrix A.


# In[ ]:


### eigenvectors of symmetric matrices

# create a random matrix
A = np.random.randn(14,14)

# make it symmetric
S = A@A.T

# diagonalize it
evals,evecs = np.linalg.eig(S)


# magnitudes of each vector
print( np.sqrt( sum(evecs**2) ) )


# In[ ]:


# and make plots
plt.imshow(S)
plt.axis('off')
plt.title('S')
plt.show()

plt.imshow(evecs)
plt.axis('off')
plt.title('Eigenvectors')
plt.show()

plt.imshow(evecs.T@evecs)
plt.axis('off')
plt.title('V$^T$V')
plt.show()


#   QUESTION: If VtV = I, then Vt = V^-1. How can you verify this in Python?
# 
# Answer: you can inspect evecs' - inv(evecs). Note that due to computer
# rounding errors, 1e-15 (10^-15) can be considered zero.


# In[ ]:


# side note about the eig() function

# numpy's eig output is different from MATLAB's eig output
# numpy returns a tuple with the first element being a vector of eigenvalues, 
# and the second element the matrix of eigenvectors
lambdas = np.linalg.eig(S)
print(len(lambdas))
print(lambdas)

# To diagonalize:
eigvals,eigvecs = np.linalg.eig(S)
print(' ')
np.diag(eigvals)


# In[ ]:


# some fun with random matrices

# Random matrices tend to have complex eigenvalues
# Those eigenvalues form a circle in the complex plane.

nIter = 150
matsize = 40
evals = np.zeros((nIter,matsize),dtype=np.complex)

for i in range(nIter):
    X = np.random.randn(matsize,matsize)
    evals[i,:] = np.linalg.eig(X)[0]
    


plt.plot(np.real(evals),np.imag(evals),'ro',markerfacecolor='k')
plt.xlabel('Real part'), plt.ylabel('Imaginary part')
plt.axis('square')
plt.show()

# Note: This is just a fun FYI; no practical applications for this course.


# In[ ]:





# ---
# # Singular value decomposition (SVD)
# ---

# In[ ]:


# Here we will show that eigendecomposition and SVD are the same thing for
# symmetric matrices (they are *not* the same for other kinds of matrices;
# this is an example of a special property of symmetric matrices).

# create a symmetric matrix
X = np.random.randn(5,5)
S = X.T@X

# take its eigendecomposition
L_eig,W_eig = np.linalg.eig(S)

# take its SVD
U_svd,S_svd,V_svd = np.linalg.svd(S)


# If they are identical, their difference should be zero:
np.round( W_eig - U_svd ,4)

# deffo not zero...


# In[ ]:


print( np.vstack( (L_eig,S_svd) ).T)
# ah, they need to be sorted ;)

sidx = np.argsort(L_eig)[::-1]

# now try again:
print(' ')
print( np.vstack( (L_eig[sidx],S_svd) ).T)


# In[ ]:


# now try the vectors
print(np.round( W_eig[:,sidx] - U_svd ,4))

# I guess some columns are zero and others not? The issue now is the sign
# uncertainty of eigenvectors:
print(' ')
print(np.round( (-W_eig[:,sidx]) - U_svd ,4))


# ---
# # SVD of Einstein
# ---

# In[ ]:


# import picture
pic = Image.open('einstein.jpg')

# let's have a look
plt.imshow(pic)
plt.show()

# we need to convert it to 2D floating-point precision
pic = np.array(pic)
pic = np.mean(pic,axis=2)
plt.imshow(pic,cmap='gray')
plt.show()


# In[ ]:


# SVD (singular value decomposition)

U,S,V = np.linalg.svd( pic )

# compute percent-variance explained sigmas
singvalspct = 100*S/sum(S)


_,axs = plt.subplots(1,3,figsize=(6,4))

# image the three matrices
axs[0].imshow(U)
axs[0].set_title('U (left singular vectors)')

axs[1].imshow(np.diag(S),vmin=0,vmax=200)
axs[1].set_title('$\Sigma$ (singular values)')

axs[2].imshow(V)
axs[2].set_title('V$^T$ (right singular vectors)')

plt.tight_layout()
plt.show()




# plot the spectrum
_,axs = plt.subplots(1,2)
axs[0].plot(S,'s-')
axs[0].set_xlim([-2,100])
axs[0].set_xlabel('Component number')
axs[0].set_ylabel('Singular value ($\sigma$)')

axs[1].plot(singvalspct,'s-')
axs[1].set_xlim([-2,100])
axs[1].set_xlabel('Component number')
axs[1].set_ylabel('Singular value (% variance)')

plt.tight_layout()
plt.show()


# In[ ]:


# reconstruct the image based on some components

#  The goal here is to recreate Einstein using a small number of the most
#   important feature dimensions.

fig,axs = plt.subplots(4,4,figsize=(7,10))

for i,ax in enumerate(axs.flatten()):
    
    # reconstruct the low-rank version of the picture
    lowapp = U[:,:i]@np.diag(S[:i])@V[:i,:]
    
    # compute its rank
    matrix_rank = np.linalg.matrix_rank(lowapp)
    
    # and visualize!
    ax.imshow(lowapp,cmap='gray')
    title = f'r={matrix_rank}\n{np.sum(singvalspct[:i]):.2f}% var.'
    ax.axis('off')
    ax.set_title(title)

plt.tight_layout()
plt.show()

# QUESTION: How many components / what percent variance do you need to
#           get a "good" (subjective) reconstruction of Einstein? 
#           Does this give you any hope for post-mortem resurrection??


# In[ ]:




