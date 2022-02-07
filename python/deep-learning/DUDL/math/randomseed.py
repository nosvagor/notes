#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Math prerequisites
# ### LECTURE: Identical randomness via seeding
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import numpy as np
import torch


# In[ ]:


# generate a few random numbers
np.random.randn(5)


# In[ ]:


# repeat after fixing the seed (old-but-still-widely-used method)
np.random.seed(17)
print(np.random.randn(5))
print(np.random.randn(5))

# [ 0.27626589 -1.85462808  0.62390111  1.14531129  1.03719047]
# [ 1.88663893 -0.11169829 -0.36210134  0.14867505 -0.43778315]


# # New seed mechanism in numpy

# In[ ]:


randseed1 = np.random.RandomState(17)
randseed2 = np.random.RandomState(20210530)

print( randseed1.randn(5) ) # same sequence
print( randseed2.randn(5) ) # different from above, but same each time
print( randseed1.randn(5) ) # same as two up
print( randseed2.randn(5) ) # same as two up
print( np.random.randn(5) ) # different every time

# [ 0.27626589 -1.85462808  0.62390111  1.14531129  1.03719047]
# [-0.24972681 -1.01951826  2.23461339  0.72764703  1.2921122 ]
# [ 1.88663893 -0.11169829 -0.36210134  0.14867505 -0.43778315]
# [ 1.15494929 -0.0015467  -0.11196868 -1.08136725  0.10265891]
# [ 2.171257    1.15231025 -1.81881234 -0.13804934  0.53983961]


# # Now in pytorch

# In[ ]:


torch.randn(5)


# In[ ]:


torch.manual_seed(17)
print( torch.randn(5) )

# torch's seed doesn't spread to numpy
print( np.random.randn(5) )

