#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: ANNs
# ### LECTURE: Comparing the number of hidden units
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import libraries
import torch
import torch.nn as nn

import numpy as np
import matplotlib.pyplot as plt


# # Import and organize the data

# In[ ]:


# import dataset (comes with seaborn)
import seaborn as sns
iris = sns.load_dataset('iris')
print( iris.head() )

# some plots to show the data
sns.pairplot(iris, hue='species')
plt.show()


# In[ ]:


# organize the data

# convert from pandas dataframe to tensor
data = torch.tensor( iris[iris.columns[0:4]].values ).float()

# transform species to number
labels = torch.zeros(len(data), dtype=torch.long)
# labels[iris.species=='setosa'] = 0 # don't need!
labels[iris.species=='versicolor'] = 1
labels[iris.species=='virginica'] = 2

labels


# # Functions to create and train the model

# In[ ]:


# Note the input into the function!
def createIrisModel(nHidden):

  # model architecture (with number of units soft-coded!)
  ANNiris = nn.Sequential(
      nn.Linear(4,nHidden),      # input layer
      nn.ReLU(),                 # activation unit
      nn.Linear(nHidden,nHidden),# hidden layer
      nn.ReLU(),                 # activation unit
      nn.Linear(nHidden,3),      # output unit
      #nn.Softmax(dim=1),        # final activation unit (here for conceptual purposes, note the CEL function)
        )

  # loss function
  lossfun = nn.CrossEntropyLoss()

  # optimizer
  optimizer = torch.optim.SGD(ANNiris.parameters(),lr=.01)

  return ANNiris,lossfun,optimizer


# In[ ]:


# a function to train the model

def trainTheModel(ANNiris):

  # initialize losses
  losses = torch.zeros(numepochs)
  ongoingAcc = []

  # loop over epochs
  for epochi in range(numepochs):

    # forward pass
    yHat = ANNiris(data)

    # compute loss
    loss = lossfun(yHat,labels)
    losses[epochi] = loss

    # backprop
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

  # final forward pass
  predictions = ANNiris(data)
    
  predlabels = torch.argmax(predictions,axis=1)
  return 100*torch.mean((predlabels==labels).float())


# # Run the experiment!

# In[ ]:


numepochs  = 150
numhiddens = np.arange(1,129)
accuracies = []

for nunits in numhiddens:

  # create a fresh model instance
  ANNiris,lossfun,optimizer = createIrisModel(nunits)

  # run the model
  acc = trainTheModel(ANNiris)
  accuracies.append( acc )


# In[ ]:


# report accuracy
fig,ax = plt.subplots(1,figsize=(12,6))

ax.plot(accuracies,'ko-',markerfacecolor='w',markersize=9)
ax.plot(numhiddens[[0,-1]],[33,33],'--',color=[.8,.8,.8])
ax.plot(numhiddens[[0,-1]],[67,67],'--',color=[.8,.8,.8])
ax.set_ylabel('accuracy')
ax.set_xlabel('Number of hidden units')
ax.set_title('Accuracy')
plt.show()


# In[ ]:





# # Additional explorations

# In[ ]:


# 1) The results here show that models with fewer than ~50 hidden units have lackluster performance. Would these models 
#    eventually learn if they were given more training epochs? Try this by re-running the experiment using 500 epochs.
#    Tip: Copy/paste the plotting code into a new cell to keep both plots. Or, take screenshots of the plots.
# 
# 2) Going back to 150 epochs, explore the effect of changing the learning rate. This doesn't need to be a full parametric
#    experiment; you can simply try is again using learning rates of .1, .01 (what we used in the video), and .001.
# 
# 3) With simple models and small datasets, it's possible to test many different parameter settings. However, larger
#    models take longer to train, and so running 128 tests is not always feasible. Modify the code to have the number of
#    hidden units range from 1 to 128 in steps of 14. Plot the results on top of the results using steps of 1 (that is, 
#    show both results in the same graph). Does your interpretation change with fewer experiment runs?

