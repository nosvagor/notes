#!/usr/bin/env python
# coding: utf-8

# # COURSE: Generate and visualize data in Python and MATLAB
# 
# ## SECTION: Descriptive statistics
# 
# ### https://www.udemy.com/course/suv-data-mxc/?couponCode=201910
# 
# ### INSTRUCTOR: sincxpress.com

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# 
# ---
# # VIDEO: Mean, median, standard deviation, variance
# ---
# 

# In[ ]:


## mean (aka average or arithmetic mean)

# some numbers
vect = [ 1,2,3,2 ]
    #    1,2,2,3
n = len(vect)


# mean by definition
meanval1 = sum(vect) / n

# mean by function
meanval2 = np.mean(vect)

print(meanval1,meanval2)


# In[ ]:


## median

# easiest to the use the built-in function
medianval = np.median(vect)

print(medianval)


# In[ ]:


## standard deviation

# first, mean-center
vectC = vect - np.mean(vect)

# then, sum of squared elements, divide by N-1, take square root
stdval1 = np.sqrt(  np.sum( vectC**2 ) / (n-1)  )

# or use the function
stdval2 = np.std(vect,ddof=1) # note the second input to provide an unbiased estimate

print(stdval1,stdval2)


# In[ ]:


## variance

# it's standard deviation squared
varval1 = stdval1**2

# or use the function
varval2 = np.var(vect,ddof=1) # again, note the second input

print(varval1,varval2)


# 
# ---
# # VIDEO: Histogram
# ---
# 

# In[ ]:


# generate some random data
data  = np.random.randn(1000)
nbins = 50

plt.hist(data,nbins)
plt.show()


# 
# ---
# # VIDEO: Interquartile range
# ---
# 

# In[ ]:


## random number data
n = 1000
data = np.random.randn(n)

# rank-transform the data and scale to 1
dataR = stats.rankdata(data)/n

# find the values closest to 25% and 75% of the distribution
q1 = np.argmin(np.abs(dataR-.25))
q3 = np.argmin(np.abs(dataR-.75))

# get the two values in the data
iq_vals = [ data[q1],data[q3] ]

# IQR is the difference between them
iqrange1 = iq_vals[1] - iq_vals[0]

# here's the scipy function
iqrange2 = stats.iqr(data)

print(iqrange1,iqrange2)


# 
# ---
# # VIDEO: Violin plot
# ---
# 

# In[ ]:


# generate data
m =   1   # mean
s =  .6   # standard deviation
n = 2000  # number of data points
data = np.exp( s*np.random.randn(n) + m )


plt.violinplot(data,showmedians=True)
plt.xlim([0,2])
plt.show()

