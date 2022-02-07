#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Overfitting, cross-validation, regularization
# ### LECTURE: Splitting data into train, devset, test
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import numpy as np
from sklearn.model_selection import train_test_split


# In[ ]:


### create fake dataset (same as in previous videos)

fakedata = np.tile(np.array([1,2,3,4]),(10,1)) + np.tile(10*np.arange(1,11),(4,1)).T
fakelabels = np.arange(10)>4
print(fakedata), print(' ')
print(fakelabels)


# # Using train_test_split

# In[ ]:


# specify sizes of the partitions
# order is train,devset,test
partitions = [.8,.1,.1]

# split the data (note the third input, and the TMP in the variable name)
train_data,testTMP_data, train_labels,testTMP_labels =                    train_test_split(fakedata, fakelabels, train_size=partitions[0])

# now split the TMP data
split = partitions[1] / np.sum(partitions[1:])
devset_data,test_data, devset_labels,test_labels =               train_test_split(testTMP_data, testTMP_labels, train_size=partitions[1])




# print out the sizes
print('Training data size: ' + str(train_data.shape))
print('Devset data size: '   + str(devset_data.shape))
print('Test data size: '     + str(test_data.shape))
print(' ')

# print out the train/test data
print('Training data: ')
print(train_data)
print(' ')

print('Devset data: ')
print(devset_data)
print(' ')

print('Test data: ')
print(test_data)


# # Splitting the data manually using numpy

# In[ ]:


# partition sizes in proportion
partitions = np.array([.8,.1,.1])
print('Partition proportions:')
print(partitions)
print(' ')

# convert those into integers
partitionBnd = np.cumsum(partitions*len(fakelabels)).astype(int)
print('Partition boundaries:')
print(partitionBnd)
print(' ')


# random indices
randindices = np.random.permutation(range(len(fakelabels)))
print('Randomized data indices:')
print(randindices)
print(' ')


# In[ ]:


# select rows for the training data
train_dataN   = fakedata[randindices[:partitionBnd[0]],:]
train_labelsN = fakelabels[randindices[:partitionBnd[0]]]

# select rows for the devset data
devset_dataN   = fakedata[randindices[partitionBnd[0]:partitionBnd[1]],:]
devset_labelsN = fakelabels[randindices[partitionBnd[0]:partitionBnd[1]]]

# select rows for the test data
test_dataN   = fakedata[randindices[partitionBnd[1]:],:]
test_labelsN = fakelabels[randindices[partitionBnd[1]:]]


# In[ ]:


# print out the sizes
print('Training data size: ' + str(train_dataN.shape))
print('Devset size: '        + str(devset_dataN.shape))
print('Test data size: '     + str(test_dataN.shape))
print(' ')

# print out the train/test data
print('Training data: ')
print(train_dataN)
print(' ')

print('Devset data: ')
print(devset_dataN)
print(' ')

print('Test data: ')
print(test_dataN)


# In[ ]:




